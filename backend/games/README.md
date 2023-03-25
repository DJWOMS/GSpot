# Games service

## Quick Start
1. Fork https://github.com/DJWOMS/GSpot.git
2. In your forked repository make new branch for e. "games" based on DJWOMS/GSpot/games
3. git clone your forked repository
4. checkout to "games"

## Setup venv
```
python -m venv venv
```
```
.\venv\Scripts\activate
```
## Install requirements
```
cd backend/games
```

```
pip install -r requirements.txt
```

### Setup pre-commit
```
pre-commit install
```

### RUN

```
docker-compose up --build
```



