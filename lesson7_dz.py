def get_list() -> list:
    return list(range(0, 1_000_000, 2))



class Solution:

    def find_target(self, list,
                    target):
                            left = 0
                            right = len(list) - 1


                            while left <= right:
                                mid = (left + right) // 2

                                if list[mid] == target:
                                    return mid

                                elif list[mid] > target:
                                    right = mid - 1

                                else:
                                    left = mid + 1


                            return -1



solution = Solution()
list = get_list()
target = 500
result = solution.find_target(list,
target)
print(result)
with open("binary_search_docs.txt",
"w", encoding="utf-8") as file:
    file.write("Бинарный поиск - это" 
 "эффективный алгоритм для поиска элемента в отсортированном списке.\n")
    file.write("Целью бинарного поиска"
"является эффективное нахождение элемента в отсортированном списке,"
"минимизируя количество необходимых "
"сравнений.\n")
    file.write("Принцип работы"
" бинарного поиска состоит в повторном"
" делении списка пополам, пока целевой"
" элемент не будет найден или не станет"
" ясно, что элемент отсутствует в"
" списке.\n")