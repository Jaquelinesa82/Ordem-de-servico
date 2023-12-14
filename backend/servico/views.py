from django.shortcuts import render

def ordem_servico_list(request):
  template_name = 'servico/ordem_servico_list.html'
  # object_list = OrdemServico.object.all()
  # context = {
  #   'object_list': object_list
  # }
  return render(request, template_name)
  
def ordem_servico_create(request, pk):
  return render(request, 'ordem_servico_form.html', {})

def ordem_servico_detail(request,pk):
  return render(request, 'ordem_servico_detail.html')
 
def ordem_servico_update(request, pk):
  ...
  
def ordem_servico_delete(request, pk):
  ...     
