class Node:
  def __init__(self, val, prev: "Node" = None, next: "Node" = None):
    self.val = val
    self.prev = prev
    self.next = next

class BrowserHistory:
  # Initializes browser hisotry from new tab. 
  # By default the starting URL will be an empty string.
  # use hmap to store the history
  def __init__(self):
    self.hmap = {}
    self.head = Node("")
    self.tail = self.head
    self.curr = self.head
    self.currentIndex = 0
  # Returns the url of the curr page.
  def current_page(self) -> str:
    return self.curr.val
  # Navigates to the "page" from the curr page. 
  # Nagivating forward should overwrite all previous forward browser history.
  def go_to(self, page:str) -> None: 
    self.curr.next = Node(page, self.curr)
    self.curr = self.curr.next
    self.tail = self.curr

    self.currentIndex += 1
    self.hmap[self.currentIndex] = self.curr

    for i in range(self.currentIndex + 1, len(self.hmap) + 1):
        self.hmap.pop(i)

    return self.curr.val

  # Navigates to the previous page visited.
  # After navigating return the URL of the curr page.
  def go_back(self) -> str:
    if self.curr and self.curr.prev:
        self.curr = self.curr.prev
        self.currentIndex -= 1
        return self.curr.val

    return ""
  # Navigates to the page ahead in browser history.
  # If there is no page ahead, do nothing.
  # After navigating return the URL of the curr page.
  def go_forward(self) -> str:
    if self.curr.next:
        self.curr = self.curr.next
        self.currentIndex += 1
        return self.curr.val

    return self.curr.val
  # Navigates backwards N pages in browser history.
  # If there are not N pages behind, then return the new tab URL which is an empty string.
  # After navigating return the URL of the curr page.
  def skip_backward(self, N: int) -> int:
    if self.currentIndex - N < 0:
        self.curr = self.head
        self.currentIndex = 0
        return self.curr.val

    self.currentIndex -= N
    self.curr = self.hmap[self.currentIndex]
    return self.curr.val
  # Navigates forward N pages in browser history.
  # If there are not N pages ahead, then go as far as you can.
  # After navigating return the URL of the curr page.
  def skip_forward(self, N:int) -> str:
    if self.currentIndex + N > len(self.hmap):
        self.curr = self.tail
        self.currentIndex = len(self.hmap)
        return self.curr.val

    self.currentIndex += N
    self.curr = self.hmap[self.currentIndex]
    return self.curr.val

def assertEqual(a, b):
        if a != b:
            print("Expected", a, "but got", b)
        else:
            print("Passed")

def test_coachable_case():
    history = BrowserHistory()
    history.go_to("leetcode.com")
    history.go_to("google.com")                					# You are in "leetcode.com". Visit "google.com"
    history.go_to("facebook.com")              					# You are in "google.com". Visit "facebook.com"
    history.go_to("youtube.com")               					# You are in "facebook.com". Visit "youtube.com"
    assertEqual(history.go_back(), "facebook.com")          		# You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    assertEqual(history.go_back(), "google.com" )  		# You are in "facebook.com", move back to "google.com" return "google.com"
    assertEqual(history.go_forward(),"facebook.com")       		# You are in "google.com", move forward to "facebook.com" return "facebook.com"
    history.go_to("linkedin.com")              					# You are in "facebook.com". Visit "linkedin.com"
    assertEqual(history.skip_forward(2), "linkedin.com")	# You are in "linkedin.com", you cannot move forward any steps.
    assertEqual(history.skip_backward(2), "google.com")

if __name__ == "__main__":
    test_coachable_case()