import json

matrix = [[39, 47, 38, 39, 38, 47, 0.777], [19, 6, 13, 6, 19, 13, 0.6984], [3, 14, 15, 3, 15, 14, 0.7612], [29, 28, 11, 28, 29, 10, 0.584], [37, 35, 24, 37, 24, 31, 0.6455], [1, 44, 43, 1, 49, 44, 0.8186], [33, 9, 16, 33, 4, 9, 0.8107], [30, 23, 8, 30, 17, 8, 0.6376], [27, 41, 45, 27, 41, 45, 0.74], [34, 48, 32, 34, 48, 32, 0.6318]]

for row in matrix:
    assert len(row) == 7
    top3_a = row[:3]
    top3_b = row[3:6]
    rho = row[6]
    assert len(set(top3_a)) == 3
    assert len(set(top3_b)) == 3
    for idx in top3_a + top3_b:
        assert 0 <= idx < 50
    assert rho < 0.95

print("All validations passed successfully!")

