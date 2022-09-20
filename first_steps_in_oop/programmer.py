class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        string = ''
        if language == self.language:
            self.skills += skills_earned
            string = f'{self.name} watched {course_name}'
        else:
            string = f'{self.name} does not know {language}'

        return string

    def change_language(self, new_language, skill_needed):
        string = ''
        if new_language != self.language:
            if skill_needed <= self.skills:
                string = f"{self.name} switched from {self.language} to {new_language}"
                self.language = new_language
            else:
                string = f"{self.name} needs {skill_needed - self.skills} more skills"
        else:
            string = f"{self.name} already knows {self.language}"
        return string


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
