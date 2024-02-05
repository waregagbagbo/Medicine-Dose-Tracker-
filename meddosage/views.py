from rest_framework import generics
from .serializers import MedicineSerializer, UserSerializer # same as forms
from .models import Medicine
from rest_framework import permissions
from .permissions import IsOwnerOnly


# create views 
class MedicineView(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOnly]
    queryset = Medicine.objects.all() # options filter,sliced or ordered by view
    serializer_class = MedicineSerializer # same as form_class in django used for validating and deserializing the input and for serializing the outpu
    
    # filter user data
    def get_queryset(self):
        user = self.request.user
        return Medicine.objects.filter(owner=user)
    

# detailview
class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOnly]
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    
    
# user create API
class UserCreate(generics.CreateAPIView):
    authentication_classes = () # to excempt UserCreate from global authentication scheme
    permission_classes = ()  # same metholody as to authentication_classess
    serializer_class = UserSerializer
    







"""# Create your views here.

class  MedicineView(ListView):
    model = Medicine
    template_name = 'medicine/medlist.html'
    paginate_by = 10 
    success_url = reverse_lazy('home')          
    
    def get_context_data(self, **kwargs):
        context = super(MedicineView,self).get_context_data(**kwargs)       
        context['medicines'] = Medicine.objects.filter().order_by('-tracked_medicine') 
         
       
        # search field section
        search_input = self.request.GET.get('search_input') or '' # the apostrophe is for an empty search
        if  search_input:
           context["medicines"] = context["medicines"].filter(tracked_medicine__startswith=search_input)        
        context['search_input'] = search_input
        return context   
        


class MedicineCreate(CreateView):
    model = Medicine
    template_name = 'medicine/create.html'
    form_class = MedicineForm
    success_url = reverse_lazy('home')  
    
    def form_valid(self,form):
        my_form = User.objects.get(user=self.request.user)
        form.instance.user= my_form.save()
        return super(MedicineCreate, self).form_valid(form)  
    
            
        
class MedicineUpdate(UpdateView):  # for edit
    model = Medicine
    template_name = 'medicine/update.html'
    form_class = MedicineForm
    success_url = reverse_lazy('home')
    
    
    
class MedicineEditView(DetailView):    # for  itemview
    model = Medicine
    template_name = 'medicine/edit.html'
      
    
class MedicineDelete(DeleteView):     # for delete
    model = Medicine
    template_name ='medicine/delete.html'
    success_url = reverse_lazy('home')"""
    
    

    

     
    
   
    
    
