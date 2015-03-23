import heapq


class RunningMedian:
    '''
    Implementation of the Running Redian algorithm based on using two heaps.

    The class supports add() method to insert next elements from a sequence
    and get_median() method to retrieve current median value.
    Implementation is based on: http://stackoverflow.com/a/10657732
    '''

    def __init__(self):
        # Implementation is based on two heaps:
        # max_heap that contains elements <= median
        # min_heap that contains elements >= median
        # While adding elements to heaps we keep the property that
        # the size of any heap is not larger than the other one by more than 1
        self.min_heap = []
        # There is no max-heap implementation in Python's standrad library
        # So it is based on min-heap with storing negative values
        self.max_heap = []

    def _balance(self):
        # Make sure that none of the heaps is larger than the second one
        # by more than 1 element
        if len(self.min_heap) - len(self.max_heap) > 1:
            element = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -element)
        elif len(self.max_heap) - len(self.min_heap) > 1:
            element = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, element)

    def add(self, element):
        # Process first two elements differently
        # the first one is just added to max_heap
        # the second one is added to max_heap and then the biggest one
        # will be moved to min_heap by balancing
        if not self.min_heap or not self.max_heap:
            heapq.heappush(self.max_heap, -element)
            self._balance()
            return

        # Add the element to the max_heap if it's smaller than its root
        # otherwise add it to min_heap
        if element <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -element)
        else:
            heapq.heappush(self.min_heap, element)
        self._balance()

    def get_median(self):
        if not self.min_heap and not self.max_heap:
            raise IndexError('No median in empty sequency')

        # If the heaps are equal that median is the mean of their root elements
        size = len(self.min_heap) + len(self.max_heap)
        if size % 2 == 0:
            return 1.0 * (self.min_heap[0] + (-self.max_heap[0])) / 2

        # If one heap is larger then the median is its root element
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
