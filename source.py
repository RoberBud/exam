
class Convert():
    def createList(self, d, seen =[]):
        if not isinstance(d, dict):
            seen.append(d)
        else:
            [[a,b]] = d.items()
            seen.append(a)
            self.createList(b,seen)
        return seen 
    
    def listToDict(self, lst, d=0):
        if not lst : return None
        if d == len(lst)-1:
            return {lst[-1]}
        
        return {lst[d]: self.listToDict(lst, d+1) }
    
    def combine(self, d):
        rev = self.createList(d, seen = [])
        rev.reverse()
        
        return self.listToDict(rev)



t= Convert()

print(t.combine({
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}))
