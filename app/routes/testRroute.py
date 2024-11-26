from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import sys
sys.path.append('D:\\DataBase\\new\\group_lab_back')
from app.database import SessionLocal
from app.models.testModel import *
from app.schema.test_schema import *


user = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.post("/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user.get("/", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@user.get("/{user_id}", response_model=UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user.put("/{user_id}", response_model=UserBase)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for var, value in vars(user_update).items():
        if value is not None:
            setattr(db_user, var, value)
    db.commit()
    return db_user


@user.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"ok": True}


category = APIRouter(prefix="/categories", tags=["Categories"])

@category.post("/", response_model=CategoryBase)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@category.get("/", response_model=List[CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories

@category.get("/{category_id}", response_model=CategoryBase)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@category.put("/{category_id}", response_model=CategoryBase)
def update_category(category_id: int, category_update: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    for var, value in vars(category_update).items():
        if value is not None:
            setattr(db_category, var, value)
    db.commit()
    return db_category

@category.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return {"ok": True}

course = APIRouter(prefix="/courses", tags=["Courses"])

@course.post("/", response_model=CourseBase)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@course.get("/", response_model=List[CourseResponse])
def read_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses

@course.get("/{course_id}", response_model=CourseBase)
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@course.put("/{course_id}", response_model=CourseBase)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    for var, value in vars(course).items():
        if value is not None:
            setattr(db_course, var, value)
    db.commit()
    return db_course

@course.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"ok": True}


chapter= APIRouter(prefix="/chapters", tags=["Chapters"])

@chapter.post("/", response_model=ChapterBase)
def create_chapter(chapter: ChapterCreate, db: Session = Depends(get_db)):
    new_chapter = Chapter(**chapter.dict())
    db.add(new_chapter)
    db.commit()
    db.refresh(new_chapter)
    return new_chapter

@chapter.get("/", response_model=List[ChapterResponse])
def read_chapters(db: Session = Depends(get_db)):
    chapters = db.query(Chapter).all()
    return chapters

@chapter.get("/{chapter_id}", response_model=ChapterBase)
def read_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter

@chapter.put("/{chapter_id}", response_model=ChapterBase)
def update_chapter(chapter_id: int, chapter: ChapterUpdate, db: Session = Depends(get_db)):
    db_chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not db_chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    for var, value in vars(chapter).items():
        if value is not None:
            setattr(db_chapter, var, value)
    db.commit()
    return db_chapter

@chapter.delete("/{chapter_id}")
def delete_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db.delete(chapter)
    db.commit()
    return {"ok": True}


material= APIRouter(prefix="/materials", tags=["Materials"])

@material.post("/", response_model=MaterialBase)
def create_material(material: MaterialCreate, db: Session = Depends(get_db)):
    new_material = Material(**material.dict())
    db.add(new_material)
    db.commit()
    db.refresh(new_material)
    return new_material

@material.get("/", response_model=List[MaterialResponse])
def read_materials(db: Session = Depends(get_db)):
    materials = db.query(Material).all()
    return materials

@material.get("/{material_id}", response_model=MaterialBase)
def read_material(material_id: int, db: Session = Depends(get_db)):
    material = db.query(Material).filter(Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

@material.put("/{material_id}", response_model=MaterialBase)
def update_material(material_id: int, material: MaterialUpdate, db: Session = Depends(get_db)):
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="Material not found")
    for var, value in vars(material).items():
        if value is not None:
            setattr(db_material, var, value)
    db.commit()
    return db_material

@material.delete("/material_id}")
def delete_material(material_id: int, db: Session = Depends(get_db)):
    material = db.query(Material).filter(Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    db.delete(material)
    db.commit()
    return {"ok": True}


assignment= APIRouter(prefix="/assignments", tags=["Assignments"])

@assignment.post("/", response_model=AssignmentBase)
def create_assignment(assignment: AssignmentCreate, db: Session = Depends(get_db)):
    new_assignment = Assignment(**assignment.dict())
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return new_assignment

@assignment.get("/", response_model=List[AssignmentResponse])
def read_assignmentss(db: Session = Depends(get_db)):
    assignments = db.query(Assignment).all()
    return assignments

@assignment.get("/{assignment_id}", response_model=AssignmentBase)
def read_assignment(assignment_id: int, db: Session = Depends(get_db)):
    assignment = db.query(Assignment).filter(Assignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment

@assignment.put("/{assignment_id}", response_model=AssignmentBase)
def update_assignment(assignment_id: int, assignment: AssignmentUpdate, db: Session = Depends(get_db)):
    db_assignment = db.query(Assignment).filter(Assignment.id == assignment_id).first()
    if not db_assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    for var, value in vars(assignment).items():
        if value is not None:
            setattr(db_assignment, var, value)
    db.commit()
    return db_assignment

@assignment.delete("/{assignment_id}")
def delete_assignment(assignment_id: int, db: Session = Depends(get_db)):
    assignment = db.query(Assignment).filter(Assignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    db.delete(assignment)
    db.commit()
    return {"ok": True}


submission= APIRouter(prefix="/submissions", tags=["Submissions"])

@submission.post("/", response_model=SubmissionBase)
def create_submission(submission: SubmissionCreate, db: Session = Depends(get_db)):
    new_submission = Submission(**submission.dict())
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return new_submission

@submission.get("/", response_model=List[SubmissionResponse])
def read_submissions(db: Session = Depends(get_db)):
    submissions = db.query(Submission).all()
    return submissions

@submission.get("/{submission_id}", response_model=SubmissionBase)
def read_submission(submission_id: int, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    return submission

@submission.put("/{submission_id}", response_model=SubmissionBase)
def update_submission(submission_id: int, submission: SubmissionUpdate, db: Session = Depends(get_db)):
    db_submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not db_submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    for var, value in vars(submission).items():
        if value is not None:
            setattr(db_submission, var, value)
    db.commit()
    return db_submission

@submission.delete("/{submission_id}")
def delete_submission(submission_id: int, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    db.delete(submission)
    db.commit()
    return {"ok": True}


test= APIRouter(prefix="/tests", tags=["Tests"])

@test.post("/", response_model=TestBase)
def create_test(test: TestCreate, db: Session = Depends(get_db)):
    new_test = Test(**test.dict())
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return new_test

@test.get("/", response_model=List[TestResponse])
def read_tests(db: Session = Depends(get_db)):
    tests = db.query(Test).all()
    return tests

@test.get("/{test_id}", response_model=TestBase)
def read_test(test_id: int, db: Session = Depends(get_db)):
    test = db.query(Test).filter(Test.id == test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test

@test.put("/{test_id}", response_model=TestBase)
def update_test(test_id: int, test: TestUpdate, db: Session = Depends(get_db)):
    db_test = db.query(Test).filter(Test.id == test_id).first()
    if not db_test:
        raise HTTPException(status_code=404, detail="Test not found")
    for var, value in vars(test).items():
        if value is not None:
            setattr(db_test, var, value)
    db.commit()
    return db_test

@test.delete("/{test_id}")
def delete_test(test_id: int, db: Session = Depends(get_db)):
    test = db.query(Test).filter(Test.id == test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    db.delete(test)
    db.commit()
    return {"ok": True}


question= APIRouter(prefix="/questions", tags=["Questions"])

@question.post("/", response_model=QuestionBase)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    new_question = Question(**question.dict())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

@question.get("/", response_model=List[QuestionResponse])
def read_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions

@question.get("/{question_id}", response_model=QuestionBase)
def read_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@question.put("/{question_id}", response_model=QuestionBase)
def update_question(question_id: int, question: QuestionUpdate, db: Session = Depends(get_db)):
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    for var, value in vars(question).items():
        if value is not None:
            setattr(db_question, var, value)
    db.commit()
    return db_question

@question.delete("/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
    return {"ok": True}


option= APIRouter(prefix="/options", tags=["Options"])

@option.post("/", response_model=OptionBase)
def create_option(option: OptionCreate, db: Session = Depends(get_db)):
    new_option = Option(**option.dict())
    db.add(new_option)
    db.commit()
    db.refresh(new_option)
    return new_option

@option.get("/", response_model=List[OptionResponse])
def read_options(db: Session = Depends(get_db)):
    options = db.query(Option).all()
    return options

@option.get("/{option_id}", response_model=OptionBase)
def read_option(option_id: int, db: Session = Depends(get_db)):
    option = db.query(Option).filter(Option.id == option_id).first()
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")
    return option

@option.put("/{option_id}", response_model=OptionBase)
def update_option(option_id: int, option: OptionUpdate, db: Session = Depends(get_db)):
    db_option = db.query(Option).filter(Option.id == option_id).first()
    if not db_option:
        raise HTTPException(status_code=404, detail="Option not found")
    for var, value in vars(option).items():
        if value is not None:
            setattr(db_option, var, value)
    db.commit()
    return db_option

@option.delete("/{option_id}")
def delete_option(option_id: int, db: Session = Depends(get_db)):
    option = db.query(Option).filter(Option.id == option_id).first()
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")
    db.delete(option)
    db.commit()
    return {"ok": True}



user_progress_router = APIRouter(prefix="/user-progress", tags=["User Progress"])

@user_progress_router.post("/", response_model=UserProgressResponse)
def create_user_progress(progress: UserProgressCreate, db: Session = Depends(get_db)):
    new_progress = UserProgress(**progress.dict())
    db.add(new_progress)
    db.commit()
    db.refresh(new_progress)
    return new_progress

@user_progress_router.get("/", response_model=List[UserProgressResponse])
def read_user_progress_routers(db: Session = Depends(get_db)):
    user_progress_routers = db.query(UserProgress).all()
    return user_progress_routers

@user_progress_router.get("/{progress_id}", response_model=UserProgressResponse)
def read_user_progress(progress_id: int, db: Session = Depends(get_db)):
    progress = db.query(UserProgress).filter(UserProgress.id == progress_id).first()
    if not progress:
        raise HTTPException(status_code=404, detail="User progress not found")
    return progress

@user_progress_router.put("/{progress_id}", response_model=UserProgressResponse)
def update_user_progress(progress_id: int, progress: UserProgressUpdate, db: Session = Depends(get_db)):
    db_progress = db.query(UserProgress).filter(UserProgress.id == progress_id).first()
    if not db_progress:
        raise HTTPException(status_code=404, detail="User progress not found")
    db_progress.update(progress.dict(exclude_unset=True))
    db.commit()
    return db_progress

@user_progress_router.delete("/{progress_id}")
def delete_user_progress(progress_id: int, db: Session = Depends(get_db)):
    progress = db.query(UserProgress).filter(UserProgress.id == progress_id).first()
    if not progress:
        raise HTTPException(status_code=404, detail="User progress not found")
    db.delete(progress)
    db.commit()
    return {"ok": True}


rating_router = APIRouter(prefix="/ratings", tags=["Ratings"])

@rating_router.post("/", response_model=RatingResponse)
def create_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    new_rating = Rating(**rating.dict())
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating

@rating_router.get("/", response_model=List[RatingResponse])
def read_rating_routers(db: Session = Depends(get_db)):
    ratings = db.query(Rating).all()
    return ratings

@rating_router.get("/{rating_id}", response_model=RatingResponse)
def read_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = db.query(Rating).filter(Rating.id == rating_id).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating

@rating_router.put("/{rating_id}", response_model=RatingResponse)
def update_rating(rating_id: int, rating: RatingUpdate, db: Session = Depends(get_db)):
    db_rating = db.query(Rating).filter(Rating.id == rating_id).first()
    if not db_rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    db_rating.update(rating.dict(exclude_unset=True))
    db.commit()
    return db_rating

@rating_router.delete("/{rating_id}")
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = db.query(Rating).filter(Rating.id == rating_id).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    db.delete(rating)
    db.commit()
    return {"ok": True}