from collections import deque


def person_is_a_seller(name):
    if person[-1] == 'm':
        return True

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'johny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['johny'] = []
search_queue = deque()
search_queue += graph['you']

while search_queue:
    person = search_queue.popleft()
    if person_is_a_seller(person):
        print(person + ' is a seller')
    else:
        search_queue += graph[person]
        print(search_queue)


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         print(pivot)
#         lower = [i for i in array[1:] if i < pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(lower) + [pivot] + quicksort(greater)
#
#
# a = [10, 5, 2, 6]
# print(quicksort(a))
