from triangleChecker import triangleChecker

def test_class():
    good_triangle = triangleChecker(2, 4, 3)
    assert good_triangle.is_triangle() == 'Ура, можно построить треугольник!'
    triangle_negative_num = triangleChecker(4, -5, 3)
    assert triangle_negative_num.is_triangle() == 'С отрицательными числами ничего не выйдет!'
    triangle_str = triangleChecker('2', 4, 5)
    assert triangle_str.is_triangle() == 'Нужно вводить только числа!'
    not_triangle = triangleChecker(1, 2, 3)
    assert not_triangle.is_triangle() == 'Жаль, но из этого треугольник не сделать.'