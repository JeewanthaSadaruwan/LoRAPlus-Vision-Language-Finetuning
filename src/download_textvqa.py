import json
from pathlib import Path
from datasets import load_dataset

ROOT = Path("data/textvqa")
DATASET = "lmms-lab-encoder/textvqa"
SEED = 42

def download_split(source_split, targets):
    print(f"\nStreaming {source_split} split...")

    dataset = load_dataset(
        DATASET,
        split=source_split,
        streaming=True
    ).shuffle(seed=SEED, buffer_size=500)

    output_files = {
        name: open(ROOT / f"{name}.jsonl", "w")
        for name in targets
    }

    counts = {name: 0 for name in targets}
    seen_images = set()

    try:
        for example in dataset:
            # Keep separate evaluation splits image-disjoint.
            image_id = str(example["image_id"])

            # Avoid reusing the same image across examples.
            if image_id in seen_images:
                continue

            target = next(
                (
                    name for name, limit in targets.items()
                    if counts[name] < limit
                ),
                None
            )

            if target is None:
                break

            seen_images.add(image_id)

            image = example["image"].convert("RGB")
            image_dir = ROOT / "images" / source_split
            image_dir.mkdir(parents=True, exist_ok=True)

            image_path = image_dir / f"{image_id}.jpg"
            image.save(image_path, quality=90)

            answers = example["answers"]

            record = {
                "question_id": example["question_id"],
                "image_id": image_id,
                "image": str(image_path),
                "question": example["question"],
                "answers": answers
            }

            output_files[target].write(
                json.dumps(record) + "\n"
            )

            counts[target] += 1

            if sum(counts.values()) % 100 == 0:
                print(f"Progress: {counts}", flush=True)

    finally:
        for file in output_files.values():
            file.close()

    assert all(
        counts[name] == limit
        for name, limit in targets.items()
    ), f"Insufficient examples: {counts}"

    print(f"Completed: {counts}")


if __name__ == "__main__":
    ROOT.mkdir(parents=True, exist_ok=True)

    download_split("train", {
        "train": 2000
    })

    download_split("validation", {
        "validation": 500,
        "test": 500
    })

    print("\nDataset preparation completed!")
