from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from flask_migrate import Migrate
import os
import sys
from sqlalchemy.orm import relationship
from sqlalchemy import event, DDL
from flask_login import UserMixin

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from app import db, app
db.metadata.clear()

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1024), unique=True, nullable=True)
    password = db.Column(db.String(1024), nullable=True)
    avatar = db.Column(db.String(1024), nullable=True)
    email = db.Column(db.String(512), unique=True, nullable=True)
    dateOfBirth = db.Column(db.DateTime(timezone=True), nullable=True)
    creationDate = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    userType = relationship("UserType")
    userTypeId = db.Column(db.Integer, ForeignKey('user_type.id'))

    def __repr__(self):
        return f'<User {self.name}>'
    

class Routine(db.Model):
    __tablename__ = 'routine'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=True)
    creationDate = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    user = relationship("User")

    userId = db.Column(db.Integer, ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<Routine {self.name}>'
        

class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=True)
    creationDate = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    user = relationship("User")
    userId = db.Column(db.Integer, ForeignKey('user.id'))

    exerciseType = relationship("ExerciseType")
    exerciseTypeId = db.Column(db.Integer, ForeignKey('exercise_type.id'))
    
    def __repr__(self):
        return f'<Exercise {self.name}>'
    
class ExerciseRoutine(db.Model):
    __tablename__ = 'exercise_routine'

    id = db.Column(db.Integer, primary_key=True)
    creationDate = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    routine = relationship("Routine")
    excercise = relationship("Exercise")

    routineId = db.Column(db.Integer, ForeignKey('routine.id'))
    excerciseId = db.Column(db.Integer, ForeignKey('exercise.id'))
    
    def __repr__(self):
        return f'<ExerciseRoutine {self.name}>'    

class ExecutionExercise(db.Model):
    __tablename__ = 'execution_exercise'

    id = db.Column(db.Integer, primary_key=True)
    creationDate = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    exercise = relationship("Exercise")

    exerciseId = db.Column(db.Integer, ForeignKey('exercise.id'))
    
    def __repr__(self):
        return f'<ExecutionExercise {self.name}>'      

class ExerciseType(db.Model):
    __tablename__ = 'exercise_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=True)
    creationDate = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    user = relationship("User")
    userId = db.Column(db.Integer, ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<ExerciseType {self.name}>'
    
class UserType(db.Model):
    __tablename__ = 'user_type'

    ADMIN = 1
    REGULAR = 2

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=True)
    creationDate = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    def __repr__(self):
        return f'<UserType {self.name}>'    
#class ExecutionExerciseRoutine(db.Model):
#    __tablename__ = 'execution_exercise_routine'

#    id = db.Column(db.Integer, primary_key=True)
#    creationDate = db.Column(db.DateTime(timezone=True),
#                           server_default=func.now())
    
#    exerciseRoutine = relationship("ExerciseRoutine", back_populates = "execution_exercise_routine")

#    exerciseRoutineId = db.Column(db.Integer, ForeignKey('exercise_routine.id'))
    
#    def __repr__(self):
#        return f'<ExecutionExerciseRoutine {self.name}>'      
            
#User.routines = relationship("Routine", order_by = Routine.id, back_populates = "user")
#User.routines = relationship("Exercise", order_by = Exercise.id, back_populates = "user")


@event.listens_for(UserType.__table__, 'after_create')
def insert_initial_values(*args, **kwargs):
    db.add(UserType(id=UserType.ADMIN, name='ADMIN'))
    db.add(UserType(id=UserType.REGULAR, name='REGULAR'))
    db.commit()

event.listen(UserType.__table__, 'after_create', insert_initial_values)

migrate = Migrate(app, db)