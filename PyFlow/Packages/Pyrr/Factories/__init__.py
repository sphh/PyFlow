from PyFlow.Packages.Pyrr import PACKAGE_NAME
from PyFlow.UI.InputWidgets import REGISTER_UI_INPUT_WIDGET_PIN_FACTORY
from PyFlow.UI.UINodeBase import REGISTER_UI_NODE_FACTORY
from PyFlow.UI.UIPinBase import REGISTER_UI_PIN_FACTORY
from PyFlow.Packages.Pyrr.Factories.PinInputWidgetFactory import getInputWidget
from PyFlow.Packages.Pyrr.Factories.UINodeFactory import createUINode
from PyFlow.Packages.Pyrr.Factories.UIPinFactory import createUIPin

REGISTER_UI_INPUT_WIDGET_PIN_FACTORY(PACKAGE_NAME, getInputWidget)
REGISTER_UI_NODE_FACTORY(PACKAGE_NAME, createUINode)
REGISTER_UI_PIN_FACTORY(PACKAGE_NAME, createUIPin)
