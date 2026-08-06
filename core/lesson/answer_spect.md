# AnswerSpec

## Назначение

AnswerSpec описывает ожидаемый результат выполнения задания.

AnswerSpec не выполняет проверку.

AnswerSpec определяет,
какой ответ считается правильным.

Monitor использует AnswerSpec
для проверки ответа студента.

---

# Ответственность

AnswerSpec отвечает только за описание правильного ответа.

AnswerSpec не знает,
кто выполняет задание.

AnswerSpec не хранит результаты проверки.

---

# Что знает AnswerSpec

AnswerSpec хранит:

- тип ответа;
- параметры проверки;
- эталонные данные;
- допустимые отклонения;
- критерии успешного выполнения.

---

# Что НЕ знает AnswerSpec

AnswerSpec не знает:

- конкретного студента;
- текущий ответ студента;
- количество попыток;
- время выполнения;
- результаты проверки;
- историю прохождения.

---

# Связи

AnswerSpec принадлежит одному Task.

Task
    │
    ▼
AnswerSpec

Monitor использует AnswerSpec
при проверке задания.

---

# Жизненный цикл

AnswerSpec создаётся Lesson Designer.

AnswerSpec сохраняется
в manifest урока.

Monitor читает AnswerSpec.

Student Platform
никогда не изменяет AnswerSpec.

---

# Почему существует AnswerSpec

Task описывает

    Что должен сделать студент?

AnswerSpec описывает

    Что считается правильным ответом?

Это разные понятия.

Например

Task

"Разгадайте японский кроссворд."

и

AnswerSpec

"Матрица должна совпасть
с эталоном."

Task не должен содержать алгоритм проверки.

---

# Возможные типы AnswerSpec

Проект должен поддерживать различные типы ответов.

Например

## NonogramSolution

Полностью заполненная матрица.

---

## CompletionPercentage

Минимальный процент правильно
решённых клеток.

Например

95%

---

## FreeText

Свободный текст.

Например

Название объекта.

---

## ExactText

Полное совпадение строки.

---

## Choice

Один вариант ответа.

---

## MultipleChoice

Несколько вариантов.

---

## FaceAttributes

Правильный набор признаков лица.

Например

- пол
- возраст
- эмоция
- направление взгляда

---

## ObjectClassification

Правильная категория объекта.

Например

- самолёт
- кошка
- человек

---

## AuthorRecognition

Правильный автор.

---

## Sequence

Последовательность действий.

---

## NumericValue

Числовой ответ
с допустимой погрешностью.

---

Список открыт
для расширения.

---

# Что не делает AnswerSpec

AnswerSpec не вычисляет результат.

AnswerSpec не сравнивает ответы.

AnswerSpec не знает,
как устроен Monitor.

AnswerSpec не открывает ресурсы.

AnswerSpec не взаимодействует
со Student Platform.

---

# Проверка ответа

Lesson Designer

↓

AnswerSpec

↓

Monitor

↓

Student Answer

↓

CheckResult

Таким образом
Lesson Designer
не содержит алгоритмов проверки.

---

# Архитектурные правила

AnswerSpec является описанием
ожидаемого результата.

Алгоритмы проверки
принадлежат Monitor.

Lesson Designer
никогда не сравнивает ответы.

Student Platform
никогда не изменяет AnswerSpec.

---

# Пример

Task

Разгадайте японский кроссворд.

↓

AssetRef

puzzle_1039

↓

AnswerSpec

type = NonogramSolution

solution = matrix

↓

Monitor

↓

Student Answer

↓

CheckResult

---

# Второй пример

Task

Что изображено?

↓

AnswerSpec

type = FreeText

accepted_answers

- cat
- kitten
- kitty

↓

Monitor

↓

Student Answer

↓

CheckResult

---

# Третий пример

Task

Определите эмоцию.

↓

AnswerSpec

type = FaceAttributes

emotion = happy

↓

Monitor

↓

Student Answer

↓

CheckResult

---

# Главное правило

Task описывает действие.

AssetRef описывает ресурс.

AnswerSpec описывает правильный результат.

Monitor выполняет проверку.

Каждая сущность отвечает только
за свою область ответственности.
