
# UD4.2d - Mixin para el contexto de creación y actualización

class CreateUpdateContextMixin:
    titulo_creacion = None
    titulo_actualizacion = None
    url_borrado = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo_creacion'] = self.titulo_creacion
        context['titulo_actualizacion'] = self.titulo_actualizacion
        context['url_borrado'] = self.url_borrado

        return context
