from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import CodeForm, CodeResultForm
from code_run.code import Code


class BaseView(TemplateView):

    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        form = CodeForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get("code")
            code = Code(code)

            result = code.check_code()
            form_result = CodeResultForm({'result': result})
            context = {'form': form, 'form_result': form_result}
            return render(request, self.template_name, context=context)

        context = {'form': form}
        return render(request, self.template_name, context=context)
