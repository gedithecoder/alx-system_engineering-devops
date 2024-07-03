#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
  command => 'pip3 install Flask==2.1.0',
  ensure   => 'installed',
  provider => 'pip3'
}
