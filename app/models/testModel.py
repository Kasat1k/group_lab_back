import sys
sys.path.append('D:\\DataBase\\new\\group_lab_back')

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Enum,Float
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    cover = Column(String)


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime)
    cover = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="courses")


class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    order_number = Column(Integer, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course", back_populates="chapters")


class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum("Video", "Image", "Text", name="material_types"), index=True)
    file_link = Column(String)
    chapter_id = Column(Integer, ForeignKey('chapters.id'))
    chapter = relationship("Chapter", back_populates="materials")


class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    title = Column(String, index=True)
    deadline = Column(DateTime)
    chapter_id = Column(Integer, ForeignKey('chapters.id'))
    chapter = relationship("Chapter", back_populates="assignments")


class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    grade = Column(Float)
    assignment = relationship("Assignment", back_populates="submissions")
    user = relationship("User", back_populates="submissions")


class Test(Base):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    chapter_id = Column(Integer, ForeignKey('chapters.id'))
    chapter = relationship("Chapter", back_populates="tests")


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    test_id = Column(Integer, ForeignKey('tests.id'))
    test = relationship("Test", back_populates="questions")


class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    is_correct = Column(Boolean)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship("Question", back_populates="options")

class UserProgress(Base):
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    chapter_id = Column(Integer, ForeignKey('chapters.id'))
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    status = Column(Enum('Not Started', 'In Progress', 'Completed', 'Deferred', name="progress_status"), default='Not Started', nullable=False)
    updated_at = Column(DateTime)
    user = relationship("User", back_populates="progresses")
    course = relationship("Course", back_populates="progresses")
    chapter = relationship("Chapter", back_populates="progresses")
    assignment = relationship("Assignment", back_populates="progresses")


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    text = Column(String)
    rating = Column(Integer)
    user = relationship("User", back_populates="ratings")
    course = relationship("Course", back_populates="ratings")
   


# Establish relationships
User.progresses = relationship("UserProgress", order_by=UserProgress.id, back_populates="user")
Course.progresses = relationship("UserProgress", order_by=UserProgress.id, back_populates="course")
Chapter.progresses = relationship("UserProgress", order_by=UserProgress.id, back_populates="chapter")
Assignment.progresses = relationship("UserProgress", order_by=UserProgress.id, back_populates="assignment")
User.ratings = relationship("Rating", order_by=Rating.id, back_populates="user")
Course.ratings = relationship("Rating", order_by=Rating.id, back_populates="course")
Category.courses = relationship("Course", order_by=Course.id, back_populates="category")
Course.chapters = relationship("Chapter", order_by=Chapter.id, back_populates="course")
Chapter.materials = relationship("Material", order_by=Material.id, back_populates="chapter")
Chapter.assignments = relationship("Assignment", order_by=Assignment.id, back_populates="chapter")
Chapter.tests = relationship("Test", order_by=Test.id, back_populates="chapter")
Assignment.submissions = relationship("Submission", order_by=Submission.id, back_populates="assignment")
Test.questions = relationship("Question", order_by=Question.id, back_populates="test")
Question.options = relationship("Option", order_by=Option.id, back_populates="question")
User.submissions = relationship("Submission", order_by=Submission.id, back_populates="user")





