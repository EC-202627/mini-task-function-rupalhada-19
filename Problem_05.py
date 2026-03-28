def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=200.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine
book_title = input()
days_overdue = int(input())
fine =  float(input())
max_fine = float(input())
fine = calculate_fine(book_title,days_overdue)
print("Book:",book_title)
print("Days overdue:",days_overdue)
print("fine: Rs.",float(fine))