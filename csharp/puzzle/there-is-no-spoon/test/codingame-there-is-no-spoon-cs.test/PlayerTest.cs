using System;
using System.Collections.Generic;
using Xunit;

namespace codingame_there_is_no_spoon_cs.test
{
    public class PlayerTest
    {
        [Fact]
        public void GetCoorValueTest()
        {
            // Arrange
            Grid grid = new Grid(4, 2);
            // Act
            grid.AddLine("0000");
            grid.AddLine("0..0");

            // Assert
            // string coorVal = grid.GetCoorValue(0,0);
            Assert.Equal("0", grid.GetCoorValue(0, 0));
            Assert.Equal(".", grid.GetCoorValue(2, 1));
            Console.WriteLine("Test GetCoorValue : OK");
        }

        [Fact]
        public void IterCoordinatesTest()
        {
            Console.WriteLine("Test IterCoordinates : ");
            // Arrange
            Grid grid = new Grid(4, 2);
            // Act
            grid.AddLine("0000");
            grid.AddLine("0..0");

            IEnumerable<int[]> iEnumCoordinates = grid.IterCoordinates();
            //To retrieve all the items from the above IEnumerator object, we cannot use foreach loop instead of that we need to invoke MoveNext() Boolean method.
            foreach (int[] coor in iEnumCoordinates)
            {
                Console.WriteLine($"coordinates : ({coor[0]}, {coor[1]}) - Value : {grid.GetCoorValue(coor[0], coor[1])}");
            }
        }

        [Fact]
        public void SyntaxTest()
        {
            Console.WriteLine("Test Syntax :");
            string line = null;
            Assert.Equal(null, line);

            line = "toto";
            Console.WriteLine(line);
        }

        [Fact]
        public void NextRightNeighboorTest()
        {
            // Arrange
            Grid grid = new Grid(4, 1);
            // Act
            grid.AddLine("0.0.");

            // Assert
            // string coorVal = grid.GetCoorValue(0,0);
            Assert.Equal(new int[]{2, 0}, grid.NextRightNeighboor(0, 0));
            Assert.Equal(null, grid.NextRightNeighboor(2, 0));
            Console.WriteLine("Test NextRightNeighboor : OK");
        }

        [Fact]
        public void NextLowerNeighboorTest()
        {
            // Arrange
            Grid grid = new Grid(4, 3);
            // Act
            grid.AddLine("0.0.");
            grid.AddLine("000.");
            grid.AddLine("0..0");
            // Assert
            Assert.Equal(new int[] { 0, 1 }, grid.NextLowerNeighboor(0, 0));
            Assert.Equal(null, grid.NextLowerNeighboor(1, 1));
            Assert.Equal(new int[] { 2, 1 }, grid.NextLowerNeighboor(2, 0));
            Console.WriteLine("Test NextLowerNeighboor : OK");
        }
    }
}
