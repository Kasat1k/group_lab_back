from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

# Схеми для моделі User
class UserBase(BaseModel):
    name: str
    email: str 
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True


class ProgressStatus(str, Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    DEFERRED = 'Deferred'

# Схеми для моделі UserProgress

class UserProgressBase(BaseModel):
    user_id: int
    course_id: int
    chapter_id: int
    assignment_id: int
    status: ProgressStatus = ProgressStatus.NOT_STARTED
    updated_at: Optional[datetime] = None

class UserProgressCreate(UserProgressBase):
    pass

class UserProgressUpdate(BaseModel):
    user_id: Optional[int] = None
    course_id: Optional[int] = None
    chapter_id: Optional[int] = None
    assignment_id: Optional[int] = None
    status: Optional[ProgressStatus] = None
    updated_at: Optional[datetime] = None

class UserProgressResponse(UserProgressBase):
    id: int

    class Config:
        from_attributes  = True

# Схеми для моделі Rating

class RatingBase(BaseModel):
    user_id: int
    course_id: int
    text: Optional[str] = None
    rating: int

class RatingCreate(RatingBase):
    pass

class RatingUpdate(BaseModel):
    user_id: Optional[int] = None
    course_id: Optional[int] = None
    text: Optional[str] = None
    rating: Optional[int] = None

class RatingResponse(RatingBase):
    id: int

    class Config:
        from_attributes  = True

# Схеми для моделі Category
class CategoryBase(BaseModel):

    title: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes  = True

# Схеми для моделі Course
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: int

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None

class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes  = True

# Схеми для моделі Chapter
class ChapterBase(BaseModel):

    title: str
    order_number: Optional[int] = None
    course_id: int

class ChapterCreate(ChapterBase):
    pass

class ChapterUpdate(BaseModel):
    title: Optional[str] = None
    order_number: Optional[int] = None
    course_id: Optional[int] = None

class ChapterResponse(ChapterBase):
    id: int

    class Config:
        from_attributes  = True

# Схеми для моделі Material
class MaterialBase(BaseModel):
    type: str
    file_link: str
    chapter_id: int

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(BaseModel):
    type: Optional[str] = None
    file_link: Optional[str] = None
    chapter_id: Optional[int] = None

class MaterialResponse(MaterialBase):
    id: int

    class Config:
        from_attributes  = True

# Схеми для моделі Assignment
class AssignmentBase(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    chapter_id: int

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    chapter_id: Optional[int] = None

class AssignmentResponse(AssignmentBase):
    id: int

    class Config:
        from_attributes  = True

# Схеми для моделі Submission
class SubmissionBase(BaseModel):
    grade: Optional[float] = None
    assignment_id: int
    user_id: int

class SubmissionCreate(SubmissionBase):
    pass

class SubmissionUpdate(BaseModel):
    grade: Optional[float] = None
    assignment_id: Optional[int] = None
    user_id: Optional[int] = None

class SubmissionResponse(SubmissionBase):
    id: int
    class Config:
        from_attributes  = True

# Схеми для моделі Test
class TestBase(BaseModel):
    description: Optional[str] = None
    chapter_id: int

class TestCreate(TestBase):
    pass

class TestUpdate(BaseModel):
    description: Optional[str] = None
    chapter_id: Optional[int] = None

class TestResponse(TestBase):
    id: int
    class Config:
        from_attributes  = True

# Схеми для моделі Question
class QuestionBase(BaseModel):
    text: str
    test_id: int

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(BaseModel):
    text: Optional[str] = None
    test_id: Optional[int] = None

class QuestionResponse(QuestionBase):
    id: int
    class Config:
        from_attributes  = True

# Схеми для моделі Option
class OptionBase(BaseModel):
    text: str
    is_correct: bool
    question_id: int

class OptionCreate(OptionBase):
    pass

class OptionUpdate(BaseModel):
    text: Optional[str] = None
    is_correct: Optional[bool] = None
    question_id: Optional[int] = None

class OptionResponse(OptionBase):
    id: int
    class Config:
        from_attributes  = True
