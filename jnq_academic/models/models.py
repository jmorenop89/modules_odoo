from odoo import models, fields, api

class AcademicCareer(models.Model):
    _name = 'academic.career'

    x_name = fields.Char(string = 'Name')
    x_code = fields.Char(string  = 'Code')

class AcademicStudent(models.Model):
    _name = 'academic.student'

    x_registry_number = fields.Char(string = 'Registry Number')
    x_name = fields.Char(string = 'Name')
    x_birthdate = fields.Date(string  = 'Birthdate')
    x_photo = fields.Binary(string = 'Photo')
    x_address = fields.Char(string = 'Address')
    x_tutor = fields.Many2one('res.partner', string = 'Tutor', domain="[('is_company','=',False)]")
    x_career = fields.Many2one('academic.career', string = 'Career')
    x_academic_course_grades_ids = fields.One2many('academic.course.grades','x_student_id',string = 'Student Course')

class AcademicCourse(models.Model):
    _name = 'academic.course'

    x_career = fields.Many2one('academic.career',string = 'Career')
    x_name = fields.Char(string = 'Name')
    #x_student_ids = fields.Many2many('academic.student','academic_student_course_rel','student_id','course_id',string = 'Course Students')
    x_academic_course_grades_ids = fields.One2many('academic.course.grades','x_course_id',string = 'Course Grade')

class AcademicCourseGrades(models.Model):
    _name = 'academic.course.grades'

    x_name = fields.Char(string = 'Name', compute = '_get_course_grades_name', store = True)
    x_course_id = fields.Many2one('academic.course',string = 'Course')
    x_student_id = fields.Many2one('academic.student',string = 'Student')
    x_grade_1 = fields.Float(string = 'Grade 1')
    x_grade_2 = fields.Float(string = 'Grade 2')
    x_grade_3 = fields.Float(string = 'Grade 3')
    x_grade_4 = fields.Float(string = 'Grade 4')
    x_grade_5 = fields.Float(string = 'Grade 5')
    x_partial_exam = fields.Float(string = 'Partials Exam')
    x_final_exam = fields.Float(string = 'Final Exam')
    x_final_grade = fields.Float()

    @api.depends('x_course_id','x_student_id')
    def _get_course_grades_name(self):
        for record in self:
            var_name = ''
            if record.x_course_id and record.x_student_id:
                var_name = str(record.x_student_id.x_registry_number) + ' ' + record.x_course_id.x_name
                record.x_name = var_name

