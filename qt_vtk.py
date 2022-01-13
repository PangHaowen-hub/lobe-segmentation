import os
from GUI_new import Ui_MainWindow
import vtkmodules.all as vtk
from PyQt5.QtWidgets import *
import sys
from unet3d.inference.predict import predict


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # 加载mask
    def load_mask(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开mask文件', '.', 'nii文件(*.nii *.nii.gz)')
        try:
            self.display_mask_3d(fname)
            self.display_img_mask(fname)
        except:
            print('mask文件错误！')

    # 加载image
    def load_img(self):
        self.img_name, _ = QFileDialog.getOpenFileName(self, '打开image文件', '.', 'nii文件(*.nii *.nii.gz)')
        try:
            self.display_img(self.img_name)
        except:
            print('image文件错误！')

    # 显示二维image
    def display_img(self, path):
        reader = vtk.vtkNIFTIImageReader()  # 实例化Reader对象
        reader.SetFileName(path)  # 指定所要读取的文件名
        reader.Update()  # 调用Update()方法促使管线执行

        ren = vtk.vtkRenderer()  # 创建一个渲染实例
        self.ui.vtkWidget.GetRenderWindow().AddRenderer(ren)  # 将渲染实例加入
        iren = self.ui.vtkWidget.GetRenderWindow().GetInteractor()  # 获取与此渲染实例关联的交互器
        iren.SetInteractorStyle(vtk.vtkInteractorStyleImage())  # 设置交互器样式，鼠标拖动旋转
        iren.Initialize()  # 交互器初始化
        self.image_viewer_a = vtk.vtkImageViewer2()
        self.image_viewer_a.SetInputData(reader.GetOutput())
        self.image_viewer_a.SetRenderWindow(self.ui.vtkWidget.GetRenderWindow())
        self.image_viewer_a.SetColorLevel(-500)
        self.image_viewer_a.SetColorWindow(1500)
        self.image_viewer_a.SetSlice(0)
        self.image_viewer_a.SetSliceOrientationToXY()  # 横断面
        self.image_viewer_a.GetImageActor().RotateX(180)  # 图片翻转180度
        self.image_viewer_a.Render()

        ren_2 = vtk.vtkRenderer()  # 创建一个渲染实例
        self.ui.vtkWidget_2.GetRenderWindow().AddRenderer(ren_2)  # 将渲染实例加入
        iren_2 = self.ui.vtkWidget_2.GetRenderWindow().GetInteractor()  # 获取与此渲染实例关联的交互器
        iren_2.SetInteractorStyle(vtk.vtkInteractorStyleImage())  # 设置交互器样式，鼠标拖动旋转
        iren_2.Initialize()  # 交互器初始化
        self.image_viewer_s = vtk.vtkImageViewer2()
        self.image_viewer_s.SetInputData(reader.GetOutput())
        self.image_viewer_s.SetRenderWindow(self.ui.vtkWidget_2.GetRenderWindow())
        self.image_viewer_s.SetColorLevel(-500)
        self.image_viewer_s.SetColorWindow(1500)
        self.image_viewer_s.SetSlice(0)
        self.image_viewer_s.SetSliceOrientationToYZ()  # 矢状面
        self.image_viewer_s.Render()

        ren_4 = vtk.vtkRenderer()  # 创建一个渲染实例
        self.ui.vtkWidget_4.GetRenderWindow().AddRenderer(ren_4)  # 将渲染实例加入
        iren_4 = self.ui.vtkWidget_4.GetRenderWindow().GetInteractor()  # 获取与此渲染实例关联的交互器
        iren_4.SetInteractorStyle(vtk.vtkInteractorStyleImage())  # 设置交互器样式，鼠标拖动旋转
        iren_4.Initialize()  # 交互器初始化
        self.image_viewer_c = vtk.vtkImageViewer2()
        self.image_viewer_c.SetInputData(reader.GetOutput())
        self.image_viewer_c.SetRenderWindow(self.ui.vtkWidget_4.GetRenderWindow())
        self.image_viewer_c.SetColorLevel(-500)
        self.image_viewer_c.SetColorWindow(1500)
        self.image_viewer_c.SetSlice(0)
        self.image_viewer_c.SetSliceOrientationToXZ()  # 冠状面
        self.image_viewer_c.Render()

        # 控制滚动条
        self.ui.verticalScrollBar.setMinimum(self.image_viewer_a.GetSliceMin())
        self.ui.verticalScrollBar.setMaximum(self.image_viewer_a.GetSliceMax())
        self.ui.verticalScrollBar.sliderMoved.connect(self.scrollMoved_img)
        self.ui.verticalScrollBar_2.setMinimum(self.image_viewer_s.GetSliceMin())
        self.ui.verticalScrollBar_2.setMaximum(self.image_viewer_s.GetSliceMax())
        self.ui.verticalScrollBar_2.sliderMoved.connect(self.scrollMoved_2_img)
        self.ui.verticalScrollBar_3.setMinimum(self.image_viewer_c.GetSliceMin())
        self.ui.verticalScrollBar_3.setMaximum(self.image_viewer_c.GetSliceMax())
        self.ui.verticalScrollBar_3.sliderMoved.connect(self.scrollMoved_3_img)

    # 显示三维mask
    def display_mask_3d(self, path):
        self.ren = vtk.vtkRenderer()  # 创建一个渲染实例
        self.ui.vtkWidget_3.GetRenderWindow().AddRenderer(self.ren)  # 将渲染实例加入
        self.iren = self.ui.vtkWidget_3.GetRenderWindow().GetInteractor()  # 获取与此渲染实例关联的交互器
        self.iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())  # 设置交互器样式，鼠标拖动旋转
        self.iren.Initialize()  # 交互器初始化

        reader = vtk.vtkNIFTIImageReader()  # 实例化Reader对象
        reader.SetFileName(path)  # 指定所要读取的文件名
        reader.Update()  # 调用Update()方法促使管线执行

        mapper = vtk.vtkGPUVolumeRayCastMapper()
        mapper.SetInputData(reader.GetOutput())

        volume = vtk.vtkVolume()
        volume.SetMapper(mapper)

        my_popacity = vtk.vtkPiecewiseFunction()  # 透明度
        my_popacity.AddPoint(0, 0.0)
        my_popacity.AddPoint(1, 1.0)

        color = vtk.vtkColorTransferFunction()  # 颜色
        color.AddRGBPoint(0, 0, 0, 0)  # 红
        color.AddRGBPoint(1, 1, 0, 0)  # 红
        color.AddRGBPoint(2, 0, 1, 0)  # 绿
        color.AddRGBPoint(3, 0, 0, 1)  # 蓝
        color.AddRGBPoint(4, 1, 1, 0)  # 黄
        color.AddRGBPoint(5, 0, 1, 1)  # 青

        my_property = vtk.vtkVolumeProperty()
        my_property.SetColor(color)
        my_property.SetScalarOpacity(my_popacity)
        my_property.ShadeOn()
        # my_property.SetInterpolationTypeToLinear()
        # my_property.SetShade(0, 1)
        my_property.SetDiffuse(0.2)  # 散射光，效果粗糙
        my_property.SetAmbient(0.6)  # 环境光，阴影效果不明显
        my_property.SetSpecular(0.2)  # 反射光，光滑
        # my_property.SetSpecularPower(1.0)
        # my_property.SetComponentWeight(0, 1)
        # my_property.SetDisableGradientOpacity(1)
        # my_property.DisableGradientOpacityOn()
        # my_property.SetScalarOpacityUnitDistance(1.0)

        volume.SetProperty(my_property)

        myCamera = vtk.vtkCamera()  # 设置相机位置及朝上方向
        myCamera.SetViewUp(0, 0, 1)
        myCamera.SetPosition(0, -1, 0)

        self.ren.SetActiveCamera(myCamera)
        self.ren.AddActor(volume)
        self.ren.SetBackground(1.0, 1.0, 1.0)
        self.ren.ResetCamera()

    # 显示二维mask和image
    def display_img_mask(self, path_mask):
        reader_img = vtk.vtkNIFTIImageReader()  # 实例化Reader对象
        reader_img.SetFileName(self.img_name)  # 指定所要读取的文件名
        reader_img.Update()  # 调用Update()方法促使管线执行

        reader_mask = vtk.vtkNIFTIImageReader()  # 实例化Reader对象
        reader_mask.SetFileName(path_mask)  # 指定所要读取的文件名
        reader_mask.Update()  # 调用Update()方法促使管线执行

        pColorTable = vtk.vtkLookupTable()
        pColorTable.SetNumberOfColors(6)  # 设置颜色数量
        pColorTable.SetTableRange((0, 5))
        pColorTable.SetTableValue(1, (1.0, 0.0, 0.0, 1.0))  # 红
        pColorTable.SetTableValue(2, (0.0, 1.0, 0.0, 1.0))  # 绿
        pColorTable.SetTableValue(3, (0.0, 0.0, 1.0, 1.0))  # 蓝
        pColorTable.SetTableValue(4, (1.0, 1.0, 0.0, 1.0))  # 黄
        pColorTable.SetTableValue(5, (0.0, 1.0, 1.0, 1.0))  # 青
        pColorTable.Build()

        ren = vtk.vtkRenderer()  # 创建一个渲染实例
        self.ui.vtkWidget.GetRenderWindow().AddRenderer(ren)  # 将渲染实例加入
        iren = self.ui.vtkWidget.GetRenderWindow().GetInteractor()  # 获取与此渲染实例关联的交互器
        iren.SetInteractorStyle(vtk.vtkInteractorStyleImage())  # 设置交互器样式，鼠标拖动旋转
        iren.Initialize()  # 交互器初始化

        self.viewer_img_a = vtk.vtkImageViewer2()
        self.viewer_img_a.SetInputConnection(reader_img.GetOutputPort())
        self.viewer_img_a.SetRenderWindow(self.ui.vtkWidget.GetRenderWindow())
        self.viewer_img_a.SetColorLevel(-500)
        self.viewer_img_a.SetColorWindow(1500)
        self.viewer_img_a.SetSlice(0)
        self.viewer_img_a.SetSliceOrientationToXY()
        self.viewer_img_a.GetImageActor().RotateX(180)  # 图片翻转180度
        self.viewer_img_a.GetRenderer().SetBackground(0, 0, 0)

        self.viewer_mask_a = vtk.vtkImageViewer2()
        self.viewer_mask_a.SetInputConnection(reader_mask.GetOutputPort())
        self.viewer_mask_a.SetRenderWindow(self.viewer_img_a.GetRenderWindow())
        self.viewer_mask_a.SetColorLevel(2.5)  # 窗位
        self.viewer_mask_a.SetColorWindow(5)  # 窗宽
        self.viewer_mask_a.SetSlice(0)
        self.viewer_mask_a.SetSliceOrientationToXY()  # 横断面
        self.viewer_mask_a.GetImageActor().RotateX(180)  # 图片翻转180度
        self.viewer_mask_a.GetRenderer().SetBackground(0, 0, 0)
        self.viewer_mask_a.GetImageActor().SetInterpolate(False)
        self.viewer_mask_a.GetImageActor().GetProperty().SetLookupTable(pColorTable)
        self.viewer_mask_a.GetImageActor().GetProperty().SetDiffuse(0.0)
        self.viewer_mask_a.GetImageActor().SetPickable(False)
        self.viewer_img_a.GetRenderer().AddActor(self.viewer_mask_a.GetImageActor())

        rwi = vtk.vtkRenderWindowInteractor()
        self.viewer_img_a.SetupInteractor(rwi)
        iren.Start()
        self.viewer_img_a.Render()
        self.viewer_mask_a.Render()

        ren_2 = vtk.vtkRenderer()  # 创建一个渲染实例
        self.ui.vtkWidget_2.GetRenderWindow().AddRenderer(ren_2)  # 将渲染实例加入
        iren_2 = self.ui.vtkWidget_2.GetRenderWindow().GetInteractor()  # 获取与此渲染实例关联的交互器
        iren_2.SetInteractorStyle(vtk.vtkInteractorStyleImage())  # 设置交互器样式，鼠标拖动旋转
        iren_2.Initialize()  # 交互器初始化

        self.viewer_img_s = vtk.vtkImageViewer2()
        self.viewer_img_s.SetInputConnection(reader_img.GetOutputPort())
        self.viewer_img_s.SetRenderWindow(self.ui.vtkWidget_2.GetRenderWindow())
        self.viewer_img_s.SetColorLevel(-500)
        self.viewer_img_s.SetColorWindow(1500)
        self.viewer_img_s.SetSlice(0)
        self.viewer_img_s.SetSliceOrientationToYZ()  # 矢状面
        self.viewer_img_s.GetRenderer().SetBackground(0, 0, 0)

        self.viewer_mask_s = vtk.vtkImageViewer2()
        self.viewer_mask_s.SetInputConnection(reader_mask.GetOutputPort())
        self.viewer_mask_s.SetRenderWindow(self.viewer_img_s.GetRenderWindow())
        self.viewer_mask_s.SetColorLevel(2.5)  # 窗位
        self.viewer_mask_s.SetColorWindow(5)  # 窗宽
        self.viewer_mask_s.SetSlice(0)
        self.viewer_mask_s.SetSliceOrientationToYZ()  # 矢状面
        self.viewer_mask_s.GetRenderer().SetBackground(0, 0, 0)
        self.viewer_mask_s.GetImageActor().SetInterpolate(False)
        self.viewer_mask_s.GetImageActor().GetProperty().SetLookupTable(pColorTable)
        self.viewer_mask_s.GetImageActor().GetProperty().SetDiffuse(0.0)
        self.viewer_mask_s.GetImageActor().SetPickable(False)
        self.viewer_img_s.GetRenderer().AddActor(self.viewer_mask_s.GetImageActor())

        rwi = vtk.vtkRenderWindowInteractor()
        self.viewer_img_s.SetupInteractor(rwi)
        iren_2.Start()
        self.viewer_img_s.Render()
        self.viewer_mask_s.Render()

        ren_4 = vtk.vtkRenderer()  # 创建一个渲染实例
        self.ui.vtkWidget_4.GetRenderWindow().AddRenderer(ren_4)  # 将渲染实例加入
        iren_4 = self.ui.vtkWidget_4.GetRenderWindow().GetInteractor()  # 获取与此渲染实例关联的交互器
        iren_4.SetInteractorStyle(vtk.vtkInteractorStyleImage())  # 设置交互器样式，鼠标拖动旋转
        iren_4.Initialize()  # 交互器初始化

        self.viewer_img_c = vtk.vtkImageViewer2()
        self.viewer_img_c.SetInputConnection(reader_img.GetOutputPort())
        self.viewer_img_c.SetRenderWindow(self.ui.vtkWidget_4.GetRenderWindow())
        self.viewer_img_c.SetColorLevel(-500)
        self.viewer_img_c.SetColorWindow(1500)
        self.viewer_img_c.SetSlice(0)
        self.viewer_img_c.SetSliceOrientationToXZ()  # 冠状面
        self.viewer_img_c.GetRenderer().SetBackground(0, 0, 0)

        self.viewer_mask_c = vtk.vtkImageViewer2()
        self.viewer_mask_c.SetInputConnection(reader_mask.GetOutputPort())
        self.viewer_mask_c.SetRenderWindow(self.viewer_img_c.GetRenderWindow())
        self.viewer_mask_c.SetColorLevel(2.5)  # 窗位
        self.viewer_mask_c.SetColorWindow(5)  # 窗宽
        self.viewer_mask_c.SetSlice(0)
        self.viewer_mask_c.SetSliceOrientationToXZ()  # 冠状面
        self.viewer_mask_c.GetRenderer().SetBackground(0, 0, 0)
        self.viewer_mask_c.GetImageActor().SetInterpolate(False)
        self.viewer_mask_c.GetImageActor().GetProperty().SetLookupTable(pColorTable)
        self.viewer_mask_c.GetImageActor().GetProperty().SetDiffuse(0.0)
        self.viewer_mask_c.GetImageActor().SetPickable(False)
        self.viewer_img_c.GetRenderer().AddActor(self.viewer_mask_c.GetImageActor())

        rwi = vtk.vtkRenderWindowInteractor()
        self.viewer_img_c.SetupInteractor(rwi)
        iren_4.Start()
        self.viewer_img_c.Render()
        self.viewer_mask_c.Render()

        self.ui.verticalScrollBar.setMinimum(self.viewer_img_a.GetSliceMin())
        self.ui.verticalScrollBar.setMaximum(self.viewer_img_a.GetSliceMax())
        self.ui.verticalScrollBar.sliderMoved.connect(self.scrollMoved)

        self.ui.verticalScrollBar_2.setMinimum(self.viewer_img_s.GetSliceMin())
        self.ui.verticalScrollBar_2.setMaximum(self.viewer_img_s.GetSliceMax())
        self.ui.verticalScrollBar_2.sliderMoved.connect(self.scrollMoved_2)

        self.ui.verticalScrollBar_3.setMinimum(self.viewer_img_c.GetSliceMin())
        self.ui.verticalScrollBar_3.setMaximum(self.viewer_img_c.GetSliceMax())
        self.ui.verticalScrollBar_3.sliderMoved.connect(self.scrollMoved_3)

        self.ui.horizontalSlider.setRange(0, 100)
        self.ui.horizontalSlider.setValue(100)
        self.ui.horizontalSlider.sliderMoved.connect(self.sliderMoved)

        self.ui.horizontalSlider_2.setRange(0, 100)
        self.ui.horizontalSlider_2.setValue(100)
        self.ui.horizontalSlider_2.sliderMoved.connect(self.sliderMoved_2)

        self.ui.horizontalSlider_3.setRange(0, 100)
        self.ui.horizontalSlider_3.setValue(100)
        self.ui.horizontalSlider_3.sliderMoved.connect(self.sliderMoved_3)

    def segmentation(self):
        model_path = './trained_models_lobe'
        os.makedirs('./temp', exist_ok=True)
        _, fullflname = os.path.split(self.img_name)
        output_path = os.path.join('./temp', fullflname[:-7] + '.nii.gz')
        predict(model_path, self.img_name, output_path)
        self.display_mask_3d(output_path)
        self.display_img_mask(output_path)

    # 滚动条改变image切片位置
    def scrollMoved_img(self):
        self.image_viewer_a.SetSlice(self.ui.verticalScrollBar.value())

    def scrollMoved_2_img(self):
        self.image_viewer_s.SetSlice(self.ui.verticalScrollBar_2.value())

    def scrollMoved_3_img(self):
        self.image_viewer_c.SetSlice(self.ui.verticalScrollBar_3.value())

    # 滚动条改变image和mask切片位置
    def scrollMoved(self):
        self.viewer_mask_a.SetSlice(self.ui.verticalScrollBar.value())
        self.viewer_img_a.SetSlice(self.ui.verticalScrollBar.value())

    def scrollMoved_2(self):
        self.viewer_img_s.SetSlice(self.ui.verticalScrollBar_2.value())
        self.viewer_mask_s.SetSlice(self.ui.verticalScrollBar_2.value())

    def scrollMoved_3(self):
        self.viewer_mask_c.SetSlice(self.ui.verticalScrollBar_3.value())
        self.viewer_img_c.SetSlice(self.ui.verticalScrollBar_3.value())

    # 滑动条改变透明度
    def sliderMoved(self):
        self.viewer_mask_a.GetImageActor().GetProperty().SetOpacity(self.ui.horizontalSlider.value() / 100.0)  # 透明度
        self.viewer_mask_a.Render()

    def sliderMoved_2(self):
        self.viewer_mask_s.GetImageActor().GetProperty().SetOpacity(self.ui.horizontalSlider_2.value() / 100.0)  # 透明度
        self.viewer_mask_s.Render()

    def sliderMoved_3(self):
        self.viewer_mask_c.GetImageActor().GetProperty().SetOpacity(self.ui.horizontalSlider_3.value() / 100.0)  # 透明度
        self.viewer_mask_c.Render()


if __name__ == "__main__":
    vtk.vtkOutputWindow.SetGlobalWarningDisplay(0)  # 屏蔽vtk报错窗口
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
