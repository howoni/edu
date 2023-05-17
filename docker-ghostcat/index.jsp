<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%
  Connection conn = null;
  PreparedStatement stmt = null;
  ResultSet rs = null;
  try {
    Class.forName("org.mariadb.jdbc.Driver");
    String url = "jdbc:mariadb://localhost:3306/mydb";
    String username = "edu";
    String password = "edu230515!@";
    conn = DriverManager.getConnection(url, username, password);
    stmt = conn.prepareStatement("SELECT * FROM users where name='Alice' or name='Bob'");
    //name=flag email="FLAG"
    rs = stmt.executeQuery();
    out.println("<html><head><title>MySQL Query Result</title></head><body><table><tr><th>ID</th><th>Name</th><th>Email</th></tr>");
    while (rs.next()) {
      out.println("<tr><td>" + rs.getInt("id") + "</td><td>" + rs.getString("name") + "</td><td>" + rs.getString("email") + "</td></tr>");
    }
    out.println("</table></body></html>");
  } catch (ClassNotFoundException | 
           SQLException e) {
    out.println("An error occurred while processing the request: " + e.getMessage());
  } finally {
    if (rs != null) {
      try {
        rs.close();
      } catch (SQLException e) {
        // Ignore
      }
    }
    if (stmt != null) {
      try {
        stmt.close();
      } catch (SQLException e) {
        // Ignore
      }
    }
    if (conn != null) {
      try {
        conn.close();
      } catch (SQLException e) {
        // Ignore
      }
    }
  }
%>

