using System;
using System.Collections;
using System.Collections.Generic;

namespace codingame_there_is_no_spoon_cs
{
    class Player
    {
        static void Main(string[] args)
        {
            int width = int.Parse(Console.ReadLine()); // the number of cells on the X axis
            int height = int.Parse(Console.ReadLine()); // the number of cells on the Y axis
            // Grid grid = new Grid(width, height);
            Grid grid = new Grid(width, height);

            for (int i = 0; i < height; i++)
            {
                grid.AddLine(Console.ReadLine());
            }

            IEnumerable<int[]> iEnumCoordinates = grid.IterCoordinates();
            foreach(int[] coor in iEnumCoordinates)
            {
                string line = null;
                if (grid.GetCoorValue(coor[0], coor[1]) == "0")
                {
                    line = $"{coor[0]} {coor[1]}";
                }
                else
                {
                    continue;
                }

                int[] nextRightCoor = grid.NextRightNeighboor(coor[0], coor[1]);
                if (nextRightCoor != null)
                {
                    line += $" {nextRightCoor[0]} {nextRightCoor[1]}";
                }
                else
                {
                    line += " -1 -1";
                }

                int[] nextLowerCoor = grid.NextLowerNeighboor(coor[0], coor[1]);
                if (nextLowerCoor != null)
                {
                    line += $" {nextLowerCoor[0]} {nextLowerCoor[1]}";
                }
                else
                {
                    line += " -1 -1";
                }
                Console.WriteLine(line);
            }
        }
    }

    public class Grid
    {
        public int width;
        public int height;
        public List<char[]> grid = new List<char[]>();

        public Grid(int width, int height)
        {
            this.width = width;
            this.height = height;
        }

        public string GetCoorValue(int x, int y)
        {
            char[] row = grid[y];
            char coorValue = row[x];
            return coorValue.ToString();
        }

        public void AddLine(string line)
        {
            grid.Add(line.ToCharArray());
        }

        public IEnumerable<int[]> IterCoordinates()
        {
            for (int row = 0; row < height; row++)
            {
                for (int col = 0; col < width; col++)
                {
                    yield return new int[] { col, row };
                }
            }
        }

        public int[] NextLowerNeighboor(int x, int y)
        {
            int[] result = null;
            y++;
            while (y < this.height)
            {
                if (this.GetCoorValue(x, y) == "0")
                {
                    result = new int[] { x, y };
                    break;
                }
                y++;
            }
            return result;
        }

        public int[] NextRightNeighboor(int x, int y)
        {
            int[] result = null;
            x++;
            while (x < this.width)
            {
                if (this.GetCoorValue(x, y) == "0")
                {
                    result = new int[] {x, y};
                    break;
                }
                x++;
            }
            return result;
        }
    }

}
