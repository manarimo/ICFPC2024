ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n"

buf = ""
str = gets
str.each_char do |c|
  buf += "#{ORDER[c.ord - 33]}"
end
puts buf
