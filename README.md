## This is the primary repository for all the machine learning applications.

## Please go to individual folders for more details on the applications

For more details about the ML application, see the [ML Application README](ml-application/README.md).


## ML Repository Structure
```bash
ml-repo/
├── ml-application/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── serve.py
│   │   └── train.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_main.py
│   ├── deployment/
│   │   └── docker-compose.yml
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
├── .github/
│   └── workflows/
│       ├── ci-cd.yml
        ├── docker-build.yml
├── .gitignore
```