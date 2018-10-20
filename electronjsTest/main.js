const {app, BrowserWindow} = require('electron');
const path = require ('path');
const url = require ('url');

let win;

// Create browser window
function createWindow()
{
  win = new BrowserWindow({width:800, height:600});

// Load index.html
  win.loadURL(url.format(
    {
      pathname: path.join('index.html'),
      protocol: 'file:',
      slashes: true
    }
  ));
  //Open devtools
  win.webContents.openDevTools();

  win.on('closed', () =>
   {
    win =null;
  });
}

//Run create window function
app.on('ready', createWindow);
//Quit when all windows are closed
app.on('window-all-closed', () => {
  if(process.platform!== 'darwin')
  {
    app.quit();
  }
})
