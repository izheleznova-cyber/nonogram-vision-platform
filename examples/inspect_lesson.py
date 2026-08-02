from core.lesson.loader import load_lesson

lesson = load_lesson(
    "../nonogram-dataset/lessons/lesson01_build"
)

print(lesson)


print(lesson.count)
