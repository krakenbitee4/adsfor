    def dump_frame_tree(self, page: Optional[Page] = None) -> None:
        """
        Рекурсивно выводит дерево фреймов.
        :param page: страница, если не передана, то используется текущая страница в атрибуте ads.page
        :return: None
        """
        if not page:
            page = self.page
        self._dump_frame_tree(page.main_frame)

    def _dump_frame_tree(self, frame: Frame, indent: str = "") -> None:
        """
        Рекурсивно выводит дерево фреймов, необходимо передать main_frame.
        :param frame: фрейм
        :param indent: отступ
        :return: None
        """
        print(indent + frame.name + '@' + frame.url)
        for child in frame.child_frames:
            self._dump_frame_tree(child, indent + "    ")

    def get_browser_offsets(self):
        """
        Получает смещение окна браузера относительно экрана
        :return: смещение окна браузера
        """
        self.page.bring_to_front()

        browser_offsets = self.page.evaluate(
            """() => ({
                x: window.screenX,
                y: window.screenY
            })"""
        )
