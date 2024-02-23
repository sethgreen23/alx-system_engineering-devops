# kills a process named killmenow

exec { 'kill killmenow':
  command => 'pkill -9 killmenow',
  provider => 'shell',
}
