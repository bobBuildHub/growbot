const UserForm = () => (
  <div className="my-4">
    <h2>Add New User</h2>
    <form>
      <input type="text" placeholder="Username" className="border p-2 mb-2" />
      <select className="border p-2 mb-2">
        <option value="admin">Admin</option>
        <option value="user">User</option>
      </select>
      <button className="bg-green-500 text-white px-4 py-2 rounded">Add User</button>
    </form>
  </div>
);

export default UserForm;
