#include "editnodewindow.h"
#include "ui_editnodewindow.h"

EditNodeWindow::EditNodeWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::EditNodeWindow)
{
    ui->setupUi(this);
}

EditNodeWindow::~EditNodeWindow()
{
    delete ui;
}
