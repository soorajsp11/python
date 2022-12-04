
#ternary statements
=begin
A shorter version of the if statement. It will evaluate an expression, if true,
it will execute the code following the ?. If false, execute the code following the :. 
=end
# Example of condition evaluating to true
age1 = 19
can_vote = (age1 >= 18) ? "You can vote." : "You can't vote."
puts can_vote
# Example of condition evaluating to false
age2 = 17
can_vote = (age2 >= 18) ? "You can vote." : "You can't vote."
puts can_vote

