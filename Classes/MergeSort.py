# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: MergeSort.py
# =================================================================================================

# Import classes
from Classes.Sorter import Sorter

# MergeSort class
class MergeSort(Sorter):
    @staticmethod
    def merge_sort(arr):
        """
        The merge_sort function takes an array as input and sorts it using the merge sort algorithm.
        The function splits the array into two halves, then recursively calls itself on each half.
        Once a half is split down to one element, it returns that element back up to its parent call. 
        When both halves are returned from their recursive calls, they are merged together in sorted order.
        This effectively sorted the given array in an efficient way.
        
        :param arr: Pass the array to be sorted
        :return: A sorted array
        """
        # If array length is more than 1 (and requires sorting)
        if len(arr) > 1:
            # Find middle of array and split into left and right half
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            # Recursive sort each half
            MergeSort.merge_sort(left_half)
            MergeSort.merge_sort(right_half)
            # Merging the sorted halves
            left_index = right_index = merged_index = 0
            # Merge the two halves
            while left_index < len(left_half) and right_index < len(right_half):
                # If the left value is less than the right half value
                if left_half[left_index] < right_half[right_index]:
                    # Take element from left half
                    arr[merged_index] = left_half[left_index]
                    # Move to the next element in left half
                    left_index += 1
                else:
                    # Take element from right half
                    arr[merged_index] = right_half[right_index]
                    # Move to the next element in right half
                    right_index += 1
                # Move to the next position in the main array
                merged_index += 1
            # Check if any elements are left in the left half
            while left_index < len(left_half):
                # Copy remaining elements from left half
                arr[merged_index] = left_half[left_index]
                # Move to the next element in left half
                left_index += 1
                # Move to the next position in the main array
                merged_index += 1
            # Check if any elements are left in the right half
            while right_index < len(right_half):
                # Copy remaining elements from right half
                arr[merged_index] = right_half[right_index]
                # Move to the next element in right half
                right_index += 1
                # Move to the next position in the main array
                merged_index += 1
        # Return sorted array
        return arr

    @staticmethod
    def sort(arr, reverse=False):
        """
        The sort function sorts the input list using merge sort and returns the sorted list.
            
        :param arr: Store the list that is to be sorted
        :param reverse: Boolean on whether to return reversed sorted list
        :return: The sorted list
        """
        # Sort the array
        MergeSort.merge_sort(arr)
        # If reverse
        if reverse:
            # Return reversed sorted array
            return arr[::-1]
        # Else return sorted array
        else:
            return arr