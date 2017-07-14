import workdot

label_to_labels, label_to_node = workdot.parse_file('test.txt')
print 'label_to_labels:', label_to_labels
assert label_to_labels == {
  'stuff': [], 'bar': ['baz', 'other thing here'], 'baz': [], 'other thing here': [],
  'other': ['stuff'], 'foo': ['bar'],
}

assert len(label_to_node) == len(label_to_labels)

assert label_to_node['foo'].params == {'style': 'filled', 'fillcolor': '#85FDFB'}
assert label_to_node['bar'].params == {'style': 'filled', 'fillcolor': '#85FDFB'}
assert label_to_node['other thing here'].params == {'style': 'filled', 'fillcolor': '#85FDFB'}
