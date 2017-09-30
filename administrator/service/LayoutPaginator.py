from django.core.paginator import Paginator


class BootstrapPaginator(Paginator):
    def __init__(self, *args, **kwargs):
        """
        :param wing_pages: How many pages will be shown before and after current page.
        """
        self.wing_pages = kwargs.pop('wing_pages', 3)
        super(BootstrapPaginator, self).__init__(*args, **kwargs)

    def _get_page(self, *args, **kwargs):
        self.page = super(BootstrapPaginator, self)._get_page(*args, **kwargs)
        return self.page

    @property
    def page_range(self):
        return range(max(self.page.number - self.wing_pages, 1),
                     min(self.page.number + self.wing_pages + 1, self.num_pages + 1))