"""
This module provides utilities for converting XML documents in the TEI format to
JSON format. It includes functionality to parse XML elements recursively and
to save the resulting JSON representation to a specified file location.
"""

from lxml import etree
import json
from typing import Union, Dict, Any


def xml_to_dict(element: etree._Element) -> Union[Dict[str, Any], str]:
  """
  Recursively converts an XML element and its children into a dictionary.

  Args:
      element: The XML element to convert.

  Returns:
      A dictionary representation of the input XML element or a string if the
      element contains only text.
  """
  if not element.getchildren():
    if element.text:
      return element.text.strip()
    else:
      return {k: v for k, v in element.items()}
  else:
    child_dict: Dict[str, Union[Dict, list]] = {}
    for child in element:
      child_result = xml_to_dict(child)
      if child.tag in child_dict:
        if not isinstance(child_dict[child.tag], list):
          child_dict[child.tag] = [child_dict[child.tag]]
        child_dict[child.tag].append(child_result)
      else:
        child_dict[child.tag] = child_result
    if element.items():
      child_dict["@attributes"] = {k: v for k, v in element.items()}
    return child_dict


def tei_to_json(input_tei_path: str, output_json_path: str) -> None:
  """
  Converts a TEI XML file to JSON format and saves the result to a specified
  file.

  Args:
      input_tei_path: The path to the TEI XML file to convert.
      output_json_path: The path to save the resulting JSON file.

  Raises:
      etree.XMLSyntaxError: If an error occurs during XML parsing.
      FileNotFoundError: If the specified TEI XML file does not exist.
      PermissionError: If there is no permission to write to the output file.
      IOError: If an I/O error occurs during file writing.
  """
  try:
    tree = etree.parse(input_tei_path)
    root = tree.getroot()
  except etree.XMLSyntaxError as e:
    print(f"XML parsing error: {e}")
    raise
  except FileNotFoundError as e:
    print(f"Input file not found: {e}")
    raise
  except Exception as e:
    print(f"Unexpected error during XML parsing: {e}")
    raise

  try:
    tei_dict = xml_to_dict(root)
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
      json.dump(tei_dict, json_file, indent=4, ensure_ascii=False)
  except PermissionError as e:
    print(f"No permission to write to file: {e}")
    raise
  except IOError as e:
    print(f"I/O error during file writing: {e}")
    raise

if __name__ == "__main__":
    tei_file_path = "../../output_teis/Advanced Automotive Fault Diagnosis.xml"
    json_file_path = "../../output_jsons/Advanced Automotive Fault Diagnosis.json"
    tei_to_json(tei_file_path, json_file_path)
