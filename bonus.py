from typing import Union, List

def count_element_lengths(arr: List[Union[str, int]]) -> List[int]:
    return [len(str(element)) for element in arr]

# Example
input_str = ["abc", "apple", "orange"]
output_str = count_element_lengths(input_str)
print(f"Input: {input_str}\nOutput: {output_str}")