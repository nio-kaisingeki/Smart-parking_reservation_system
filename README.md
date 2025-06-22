# Smart Parking Reservation System

This is a small example project used for Cypress testing. A minimal Express
server serves a login page so the tests have something to interact with.

## Running with Docker

1. Build and start the application:

```bash
docker compose up --build
```

The server listens on [http://localhost:3000](http://localhost:3000).

2. Run Cypress tests inside the container:

```bash
docker compose run app npm test
```
