/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */
/**
 * Prepare the guestbook entry to be persisted
 */
function main(params) {
  if (!params.name || !params.email || !params.vote) {
    return Promise.reject({ error: 'no name or comment'});
  }

  return {
    doc: {
     _id: params.email,
      createdAt: new Date(),
       name: params.name,
       email: params.email,
       vote: params.vote
    }
  };
}
