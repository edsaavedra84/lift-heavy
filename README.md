# Lift Heavy - Smart Workout Tracker

A workout tracking application with webhook integration for home automation and IoT systems. Track your lifts, time your exercises, and trigger external services based on your workout events.

## Overview

Lift Heavy is a full-stack workout tracking solution that combines traditional exercise logging with modern home automation capabilities. Whether you want to dim your lights when you start a workout, track your progress over time, or integrate your fitness routine with your smart home, Lift Heavy provides the flexibility to do it all.

### Key Features

**Core Functionality:**
- Exercise tracking (weight, reps, time)
- Custom exercise types and definitions
- Workout routines with multiple exercises
- User authentication and profiles
- Exercise history and progress tracking

**Smart Integration:**
- Webhook support for external services
- Trigger events on:
  - Workout start/stop
  - Exercise timer start/stop
  - App open/close
- Perfect for home automation systems

## Architecture

### Tech Stack

**Backend:**
- Python 3.11+ with Flask web framework
- MySQL 8.0 database
- SQLAlchemy ORM with Flask-Migrate for migrations
- Flask-Login for authentication
- Cerberus for input validation

**Mobile:**
- React Native with Expo
- TypeScript
- Cross-platform (iOS, Android, Web)

### Project Structure

```
lift-heavy/
├── backend/
│   ├── app.py                    # Flask application entry point
│   ├── model/
│   │   ├── Models.py             # SQLAlchemy models
│   │   └── migrations/           # Alembic database migrations
│   ├── routes/
│   │   ├── GeneralRoutes.py      # Core route initialization
│   │   └── UserRoutes.py         # User authentication endpoints
│   └── utils/
│       ├── GenericResponses.py   # Standardized API responses
│       └── ValidationRules.py    # Request validation schemas
├── mobile/
│   └── lift-heavy-mobile/        # React Native Expo app
└── docker-compose.yaml           # MySQL database container
```

### Database Schema

**Core Entities:**
- **User** - User accounts with authentication
- **UserType** - Admin and regular user roles
- **Exercise** - Individual exercises (e.g., "Barbell Bench Press")
- **ExerciseType** - Categories of exercises (e.g., "Chest", "Legs")
- **Routine** - User-defined workout routines
- **ExerciseRoutine** - Links exercises to routines
- **ExecutionExercise** - Records of completed exercise sessions

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Node.js 16+ and npm
- Docker and Docker Compose (for MySQL)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/lift-heavy.git
   cd lift-heavy
   ```

2. **Start the database:**
   ```bash
   docker-compose up -d
   ```

3. **Set up the backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   flask db upgrade
   python app.py
   ```

4. **Set up the mobile app:**
   ```bash
   cd mobile/lift-heavy-mobile
   npm install
   npm start
   ```

### Development

**Backend API:**
```bash
cd backend
python app.py
# API available at http://127.0.0.1:5000
```

**Mobile App:**
```bash
cd mobile/lift-heavy-mobile
npm start        # Start Expo dev server
npm run android  # Run on Android emulator/device
npm run ios      # Run on iOS simulator/device
npm run web      # Run in browser
```

**Database Migrations:**
```bash
cd backend
flask db migrate -m "Description of changes"
flask db upgrade
```

## API Endpoints

### Authentication

- `POST /register` - Create new user account
  - Body: `{ username, email, password, dateOfBirth }`
  - Date format: `MM/DD/YYYY`

- `POST /login` - Authenticate user
  - Body: `{ username/email, password }`

- `GET /profile` - Get current user profile (requires authentication)

- `GET /confirm` - Email confirmation endpoint (planned)

## Configuration

### Database Connection

Default MySQL configuration (configured in `docker-compose.yaml`):
- Host: `127.0.0.1:3306`
- Database: `lift_heavy`
- User: `root`
- Password: `secret`

### Security Note

⚠️ The current setup uses hardcoded credentials for development. Before deploying to production:
- Set `SECRET_KEY` via environment variable
- Use secure database credentials
- Enable HTTPS
- Configure proper session storage

## Roadmap

- [ ] Complete mobile UI implementation
- [ ] Webhook configuration and management
- [ ] Exercise execution tracking with timers
- [ ] Progress charts and analytics
- [ ] Social features and workout sharing
- [ ] Export workout data
- [ ] Integration guides for popular home automation platforms

## Contributing

Contributions are welcome! This is a learning project focused on React Native development and full-stack architecture.

## License

This project is open source and available for personal and educational use.

## Motivation

This project serves as a hands-on learning experience for React Native development while building something genuinely useful. The webhook integration makes it unique - imagine your home lights adjusting automatically when you start a workout, or your smart speaker announcing when it's time for your next set!
