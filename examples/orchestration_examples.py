# Example APIs and orchestration snippets

## 1. Candidate proposal example

```python
class CandidateGenerator:
    def __init__(self, model):
        self.model = model

    def generate_candidates(self, n: int = 20):
        return self.model.sample(n)
```

## 2. Active learning / acquisition example

```python
class AcquisitionOptimizer:
    def __init__(self, surrogate):
        self.surrogate = surrogate

    def propose(self, candidates, n: int = 10):
        scores = self.surrogate.rank(candidates)
        return sorted(candidates, key=lambda x: scores[x], reverse=True)[:n]
```

## 3. Experiment ingestion example

```python
class AssayResultIngestor:
    def __init__(self, lims_client):
        self.lims_client = lims_client

    def store(self, sample_id: str, readout: dict):
        self.lims_client.store_assay_result(sample_id, readout)
```

## 4. Closed-loop orchestration example

```python
class ClosedLoopPipeline:
    def __init__(self, generator, optimizer, lims, assay_platform):
        self.generator = generator
        self.optimizer = optimizer
        self.lims = lims
        self.assay_platform = assay_platform

    def run_cycle(self):
        candidates = self.generator.generate_candidates()
        prioritized = self.optimizer.propose(candidates, n=10)
        sample_ids = self.lims.register_samples(prioritized)
        results = self.assay_platform.run(sample_ids)
        self.lims.store_results(results)
        self.optimizer.update(results)
        return results
```

## 5. Example JSON schema for assay data

```json
{
  "sample_id": "CMPD_0001",
  "molecule": "CCOCCN1C=NC2=CC=CC=C2C1=O",
  "assay_type": "cell_viability",
  "readout": {
    "ic50": 0.42,
    "ec50": 0.18,
    "viability_48h": 83.2
  },
  "metadata": {
    "plate_id": "PLATE_2026_01",
    "replicate": 3,
    "instrument": "plate_reader_01"
  }
}
```
