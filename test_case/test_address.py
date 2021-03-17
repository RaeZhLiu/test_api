from base_page.address import Department


class TestCase(object):
    def setup(self):
        self.department = Department()

    def test_get_department_list(self):
        print(self.department.get_department_list())

    def test_create(self):
        print(self.department.create_department("青岛研发中心", "1"))

    def test_update(self):
        print(self.department.update_department("6", "黄岛研发中心"))

    def test_delete(self):
        print(self.department.delete_department("6"))