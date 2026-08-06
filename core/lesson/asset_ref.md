# AssetRef

## Назначение

AssetRef представляет ссылку на учебный ресурс.

AssetRef не содержит сам ресурс.

AssetRef используется для связи задания (Task)
с существующим Asset.

Это позволяет использовать один и тот же ресурс
в различных уроках без копирования данных.

---

# Ответственность

AssetRef отвечает только за связь
между Task и Asset.

AssetRef не хранит учебный материал.

AssetRef не знает,
как устроен Asset.

---

# Что знает AssetRef

AssetRef хранит:

- asset_id;
- роль ресурса;
- параметры использования;
- параметры отображения.

Например:

- масштаб;
- режим открытия;
- режим просмотра;
- дополнительные локальные настройки.

---

# Что НЕ знает AssetRef

AssetRef не знает:

- содержимое Asset;
- паспорт Asset;
- путь к файлу;
- миниатюру;
- статистику использования;
- ответы студентов;
- результаты проверки.

---

# Связи

AssetRef принадлежит одному Task.

Task
    │
    ▼
AssetRef
    │
    ▼
Asset

Asset может использоваться
любым количеством AssetRef.

                Asset
                  ▲
                  │
        ┌─────────┼─────────┐
        │         │         │
    AssetRef  AssetRef  AssetRef

---

# Жизненный цикл

AssetRef создаётся Lesson Designer.

AssetRef сохраняется
в manifest урока.

Monitor использует AssetRef
для поиска соответствующего Asset.

Student Platform работает
с уже найденным Asset.

---

# Почему существует AssetRef

Asset является независимым объектом системы.

Если хранить Asset внутри Task,
то один и тот же ресурс будет копироваться
во множество уроков.

Например

Lesson A

↓

Task

↓

Asset

--------------------

Lesson B

↓

Task

↓

Asset

Получится две копии одного и того же ресурса.

Это нарушает принцип единственного источника данных.

Использование AssetRef устраняет эту проблему.

---

# Использование Monitor

Monitor получает

Task

↓

AssetRef

↓

asset_id

↓

PassportDatabase

↓

Asset

↓

Student Platform

Таким образом Lesson Designer
никогда не загружает ресурс самостоятельно.

---

# Использование PassportDatabase

AssetRef знает только

asset_id.

PassportDatabase отвечает
за поиск соответствующего Asset.

Если Asset отсутствует,
ошибка обнаруживается Monitor
или Validator.

---

# Что не делает AssetRef

AssetRef не открывает файл.

AssetRef не читает Passport.

AssetRef не выполняет поиск.

AssetRef не знает,
где физически расположен ресурс.

AssetRef не содержит изображение.

AssetRef не содержит миниатюру.

AssetRef не выполняет проверку задания.

---

# Возможные роли ресурса

В будущем один Task
может использовать несколько ресурсов.

Например

Основной ресурс

Reference

Template

Example

Answer

Mask

Annotation

Поэтому AssetRef
может хранить роль использования ресурса.

---

# Архитектурные правила

AssetRef всегда ссылается
на существующий Asset.

AssetRef никогда
не содержит копию Asset.

AssetRef является частью Lesson.

Asset принадлежит базе ресурсов.

Удаление Lesson
не удаляет Asset.

Удаление Asset
должно проверяться Validator,
если существуют AssetRef.

---

# Пример

PassportDatabase

↓

Asset

id = puzzle_1039

↓

Lesson

↓

Stage

↓

Task

↓

AssetRef

asset_id = puzzle_1039

↓

Monitor

↓

PassportDatabase.find(asset_id)

↓

Asset

↓

Student Platform
