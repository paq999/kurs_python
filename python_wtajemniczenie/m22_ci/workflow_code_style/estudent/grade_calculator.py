from collections.abc import Sequence

from estudent.grade import Grade


class GradeCalculator:

    MAX_FAILING_GRADES_TO_PASS = 2
    MIN_AVERAGE_TO_PASS_STRICT_POLICY = 3

    @staticmethod
    def normal_promotion_policy(final_grades: Sequence[Grade]) -> bool:
        failing_grades = GradeCalculator.get_number_of_failing_grades(final_grades)
        if failing_grades > GradeCalculator.MAX_FAILING_GRADES_TO_PASS:
            return False
        return True

    @staticmethod
    def trivial_promotion_policy(final_grades: Sequence[Grade]) -> bool:
        for grade in final_grades:
            if grade.is_passing():
                return True
        return False

    @staticmethod
    def strict_promotion_policy(final_grades: Sequence[Grade]) -> bool:
        failing_grades = GradeCalculator.get_number_of_failing_grades(final_grades)
        if failing_grades > GradeCalculator.MAX_FAILING_GRADES_TO_PASS:
            return False
        if GradeCalculator.calculate_student_avg(final_grades) < GradeCalculator.MIN_AVERAGE_TO_PASS_STRICT_POLICY:
            return False
        return True

    @staticmethod
    def get_number_of_failing_grades(grades: Sequence[Grade]) -> int:
        failing_grades = 0
        for grade in grades:
            if not grade.is_passing():
                failing_grades += 1
        return failing_grades

    @staticmethod
    def calculate_student_avg(final_grades: Sequence[Grade]) -> float:
        grade_sum = 0
        for grade in final_grades:
            grade_sum += grade.value
        return grade_sum / len(final_grades)
