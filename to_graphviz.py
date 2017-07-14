#!/usr/bin/python
import os, sys

class Node:
  def __init__(self):
    self.params = {}

def main():
  in_path = os.path.expanduser(sys.argv[1])
  write_to_graphviz(*parse_file(in_path))

def parse_file(path):
  with open(path) as f:
    text = f.read()

  depth_label_pairs = []
  label_to_labels = {}
  label_to_node = {}
  for line in text.splitlines():
    if not line.strip().startswith('- '):
      continue
    curr_depth, curr_label = parse_node(line, label_to_node)

    while depth_label_pairs:
      prev_depth, prev_label = depth_label_pairs[-1]
      if curr_depth > prev_depth:
        break
      depth_label_pairs.pop()
    if not depth_label_pairs:
      prev_label = None
    if prev_label is not None and prev_label not in label_to_labels.get(curr_label, []):
      label_to_labels[prev_label].append(curr_label)
    label_to_labels.setdefault(curr_label, [])
    depth_label_pairs.append((curr_depth, curr_label))
  return label_to_labels, label_to_node

def parse_node(line, label_to_node):
  spaces_str, raw_label = line.split('- ', 1)
  curr_depth = len(spaces_str)
  curr_label = raw_label.rstrip('*')
  label_to_node.setdefault(curr_label, Node())
  if raw_label.endswith('*'):
    label_to_node[curr_label].params = {
      'style': 'filled',
      'fillcolor': '#85FDFB',
    }
  return curr_depth, curr_label

def write_to_graphviz(label_to_labels, label_to_node):
  def each_line():
    for label1, connected in label_to_labels.iteritems():
      node = label_to_node[label1]
      esc_label1 = label1.replace('"', '\"')
      node_params = ['{}="{}"'.format(key, val) for key, val in node.params.iteritems()]
      full_params_str = ', '.join(node_params)
      yield '  "{}" [{}]'.format(esc_label1, full_params_str)
      for label2 in connected:
        esc_label2 = label2.replace('"', '\"')
        yield '  "{}" -- "{}"'.format(esc_label1, esc_label2)

  out_text = '\n'.join(
    ['graph G {'] +
    list(each_line()) +
    ['}']
  )
  out_path = sys.argv[2]
  with open(out_path, 'w') as f:
    f.write(out_text)

if __name__ == '__main__':
  main()
