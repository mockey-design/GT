import numpy as numpy
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
from matplotlib.ticker import AutoMinorLocator


def main():
    
    
    if len(sys.argv) != 2:
        
        print('Usage: python3 graph_edit.py <path>')
        exit(1)
    
    file_path = sys.argv[1]
    parent_path = os.path.dirname(file_path)
    new_path = os.path.join(parent_path,'updated_log_228.csv')
    
    df = process_data(file_path)
    df.to_csv(new_path,index=False)
    print('"Saved "updated_log_228.csv" successfully"')
    plot_data(df,parent_path)

def process_data(path):
    
    df = pd.read_csv(path)
    sensor_pairs = [['Sensor Data 1','Sensor Data 10'],['Sensor Data 6','Sensor Data 10'],['Sensor Data 7','Sensor Data 9'],['Sensor Data 11','Sensor Data 20'],
                    ['Sensor Data 16','Sensor Data 20'],['Sensor Data 17','Sensor Data 19'],
                    ['Sensor Data 21','Sensor Data 30'],['Sensor Data 26','Sensor Data 30'],['Sensor Data 27','Sensor Data 29'],
                    ['Sensor Data 31','Sensor Data 40'],['Sensor Data 36', 'Sensor Data 40'],['Sensor Data 37', 'Sensor Data 39'],
                    ['Sensor Data 41','Sensor Data 50'],['Sensor Data 46','Sensor Data 50'],['Sensor Data 47','Sensor Data 49']]
   
    for first_col, second_col in sensor_pairs:
        temp = df[first_col].copy()  # 一時的な変数に最初の列の値を保存
        df[first_col] = df[second_col]
        df[second_col] = temp
    
    new_df = df.drop(['Sensor Data 31','Sensor Data 32','Sensor Data 41','Sensor Data 42'],axis=1)
    
    sensor_columns = new_df.columns[6:]
    new_column_names = {sensor_columns[i]: f'Sensor Data {i+1}' for i in range(5, len(sensor_columns))}

    final_df = new_df.rename(columns=new_column_names)
    
    return final_df
    
    
def plot_data(df,path):
    
    fig,axes = plt.subplots(2,3,figsize=(39,21))
    save_path = os.path.join(path,'sensor_plot.png')
    sensor_data = [[f"Sensor Data {i}" for i in range(1,11)],
    [f"Sensor Data {i}" for i in range(11,21)],
    [f"Sensor Data {i}" for i in range(21,31)],
    [f"Sensor Data {i}" for i in range(31,38)],
    [f"Sensor Data {i}" for i in range(39,47)]]
    
    plt.subplots_adjust(hspace=0.5,wspace=0.5)
    fig.suptitle("Sensor Data Visualization")
    
    
    for i,sensor_range in enumerate(sensor_data):
        
        ax = axes[i//3,i%3]
        
        for j,sensor_name in enumerate(sensor_range):
            ax.plot(df[sensor_name], label=sensor_name, color=cm.jet(j*10 / 100))
            
            ax.set_title(f'Sensor Data {sensor_range[0]} - {sensor_range[-1]}')
            ax.legend(loc='upper left',bbox_to_anchor=(1, 1))
            
            # グリッドを表示
            ax.grid(True)

            # Add minor ticks functionality
            ax.minorticks_on()
            ax.xaxis.set_minor_locator(AutoMinorLocator(10))
            ax.yaxis.set_minor_locator(AutoMinorLocator(10))
            ax.grid(True, which='both', linestyle='--', color='grey', alpha=0.5)
        axes[-1,-1].axis('off')
        plt.tight_layout(rect=[0, 0, 0.85, 1])
        plt.savefig(save_path,dpi = 300)
    print('"Saved "sensor_plot.png" successfully"')

if __name__ == '__main__':
    main()
