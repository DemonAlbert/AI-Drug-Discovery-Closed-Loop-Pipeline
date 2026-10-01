# Project Structure and File Organization

```
AI-Drug-Discovery-Closed-Loop-Pipeline/
│
├── README.md                                    # Project overview and high-level architecture
├── architecture.md                              # Detailed system architecture
├── stack.md                                     # Recommended open-source components
├── roadmap.md                                   # Phased implementation roadmap
├── data_models.md                               # JSON schemas for data contracts
├── repository_registry.md                       # Complete registry of all referenced repos
├── implementation_guide.md                      # Step-by-step implementation instructions
│
├── docs/
│   ├── API_SPECIFICATION.md                    # Detailed REST API documentation
│   ├── DATA_LINEAGE.md                         # Data provenance and traceability
│   ├── MULTI_OBJECTIVE_OPTIMIZATION.md         # Multi-objective design strategies
│   └── SAFETY_AND_GOVERNANCE.md                # Safety, reproducibility, audit trails
│
├── examples/
│   ├── orchestration_examples.py               # Core API pseudocode examples
│   ├── design_engine_example.py                # Molecular generation workflow
│   ├── active_learning_example.py              # Bayesian optimization loop
│   ├── lims_integration_example.py             # LIMS registration and data sync
│   ├── closed_loop_cycle.py                    # Full end-to-end cycle example
│   └── test_pipeline.py                        # Integration testing script
│
├── config/
│   ├── docker-compose.yml                      # Complete stack deployment
│   ├── .env.example                            # Environment configuration template
│   ├── lims_schema.json                        # LIMS database schema
│   └── assay_definitions.json                  # Assay protocol definitions
│
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── gateway.py                          # Main Flask API gateway
│   │   ├── pipeline_orchestrator.py            # Cycle coordination logic
│   │   └── data_manager.py                     # Central data handling
│   │
│   ├── design/
│   │   ├── __init__.py
│   │   ├── generator.py                        # Wrapper for generative models
│   │   ├── scorer.py                           # Scoring and filtering logic
│   │   └── molecular_filters.py                # ADMET and property filters
│   │
│   ├── optimization/
│   │   ├── __init__.py
│   │   ├── surrogate_model.py                  # GP / Bayesian model
│   │   ├── acquisition.py                      # Acquisition functions
│   │   └── optimizer.py                        # BO orchestration
│   │
│   ├── lims/
│   │   ├── __init__.py
│   │   ├── connector.py                        # LIMS API client
│   │   ├── sample_manager.py                   # Sample registration
│   │   └── result_ingestion.py                 # Result processing
│   │
│   ├── assay/
│   │   ├── __init__.py
│   │   ├── platform_adapter.py                 # Generic assay platform interface
│   │   ├── tecan_adapter.py                    # Example: Tecan robot
│   │   └── plate_designer.py                   # Plate layout generation
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logging.py                          # Logging configuration
│       ├── data_validation.py                  # Schema validation
│       └── converters.py                       # SMILES/feature conversions
│
├── tests/
│   ├── test_design_engine.py
│   ├── test_active_learning.py
│   ├── test_lims_integration.py
│   ├── test_assay_platform.py
│   ├── test_closed_loop.py
│   └── integration_tests.py
│
├── models/
│   ├── pretrained_generator_v1.pkl            # Pre-trained generative model
│   ├── gp_surrogate_checkpoint.pkl            # GP model checkpoint
│   └── model_registry.json                     # Model metadata and versioning
│
├── notebooks/
│   ├── 01_exploratory_design_space.ipynb      # Design space exploration
│   ├── 02_initial_model_training.ipynb        # Surrogate model training
│   ├── 03_closed_loop_validation.ipynb        # Loop validation and benchmarks
│   └── 04_results_analysis.ipynb              # Post-campaign analysis
│
├── scripts/
│   ├── setup_environment.sh                    # Initial setup script
│   ├── deploy_stack.sh                         # Docker deployment automation
│   ├── run_cycle.sh                            # Single cycle execution
│   ├── monitor_pipeline.py                     # Real-time monitoring
│   └── backup_and_export.py                    # Data export and backup
│
├── docs_external/
│   ├── CONTRIBUTING.md                         # Contribution guidelines
│   ├── LICENSE                                 # Project license (MIT/Apache/GPL)
│   └── CHANGELOG.md                            # Version history and updates
│
└── .gitignore
```

## Directory Purpose Summary

| Directory | Purpose |
|-----------|---------|
| `docs/` | Extended technical documentation |
| `examples/` | Working code examples and templates |
| `config/` | Configuration files and deployment specs |
| `src/` | Source code for the orchestration layer |
| `tests/` | Unit and integration tests |
| `models/` | Pre-trained ML models and checkpoints |
| `notebooks/` | Jupyter notebooks for exploration and analysis |
| `scripts/` | Automation and deployment scripts |

## Key Files to Start With

1. **For understanding the system**:
   - `README.md` → `architecture.md` → `stack.md`

2. **For implementation**:
   - `implementation_guide.md` → `examples/closed_loop_cycle.py` → `src/core/gateway.py`

3. **For reference**:
   - `repository_registry.md` → Individual repo links
   - `data_models.md` → Schema definitions

4. **For deployment**:
   - `config/docker-compose.yml` → `scripts/deploy_stack.sh`

## Development Workflow

```
1. Clone this repo
2. Follow implementation_guide.md (Step 1-2)
3. Start with examples/ folder
4. Adapt src/ code for your specific needs
5. Configure config/ files for your infrastructure
6. Deploy with scripts/ automation
7. Test with tests/ suite
8. Monitor and iterate
```

## Integration Checklist

- [ ] NeuThera or generative model integrated
- [ ] Zane active learning module loaded
- [ ] SENAITE LIMS connected and tested
- [ ] eLabFTW ELN configured
- [ ] Flask API gateway running
- [ ] Docker stack deployed
- [ ] First cycle executed successfully
- [ ] Data flowing through feedback loop
- [ ] Model retraining working
- [ ] Monitoring and logging active
