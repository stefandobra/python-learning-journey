# def longest_series_of_neighbours(numbers: list):
#     count = 0
#     new_list = []
#     series_lenght = 0
#     max_length = 0
#     while count < len(numbers):
#         if max_length < series_lenght:
#             max_length = series_lenght
#         if count == len(numbers) - 1:
#             break
            
#         if abs(numbers[count] - numbers[count + 1]) == 1:
#             if new_list == []:
#                 new_list.append(numbers[count])
#                 new_list.append(numbers[count+1])
#                 series_lenght += 2
                
#             else:
#                 new_list.append(numbers[count])
#                 series_lenght += 1
                
#         else:
#             series_lenght = 0
#             new_list.clear()
#         count += 1


def longest_series_of_neighbours(numbers: int):
    longest = 1
    current = 1

    for i in range(1, len(numbers)):
        if abs(numbers[i - 1] - numbers[i]) == 1:
            current += 1
        else:
            current = 1
        
        longest = max(longest, current) 



    return longest



