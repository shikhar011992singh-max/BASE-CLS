class Chai:
      def __init__(self,type_,strength):
            self.type = type_
            self.strength = strength

class gingerchai(Chai):
      def __init__(self,type_,spice_level): # CODE DUPLICATION frm lines 2-4
            self.type = type_ 
            self.spice_level = spice_level